#!/usr/bin/env python3
"""
Shorten file names (and optionally directory names) to satisfy length limits.

Defaults:
- Max file/directory segment length = 255
- Max full path length = 240 (safe for Windows + Git tooling)

Usage (dry run):
  py scripts\\shorten_file_names.py

Apply changes:
  py scripts\\shorten_file_names.py --apply

Exclude vendor path and .venv:
  py scripts\\shorten_file_names.py
  --exclude "^src/_vendor(/|$)" --exclude "^\\.venv(/|$)"

Also shorten directory names:
  py scripts\\shorten_file_names.py --shorten-dirs --apply
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

DEFAULT_MAX_NAME = 255  # typical filesystem segment limit
DEFAULT_MAX_TOTAL = 200  # safer for Windows + Git tooling


def to_rel(path: Path, root: Path) -> str:
    try:
        rel = path.relative_to(root).as_posix()
    except Exception:
        rel = path.as_posix()
    return rel


def compile_patterns(patterns: Iterable[str]) -> List[re.Pattern]:
    return [re.compile(p) for p in patterns]


def is_excluded(rel_path: str, compiled: List[re.Pattern]) -> bool:
    return any(p.search(rel_path) for p in compiled)


def short_hash(text: str, length: int = 8) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:length]


def shorten_segment(
    name: str, max_len: int, keep_ext: bool = True, min_base: int = 8
) -> str:
    """
    Shorten a file or directory name to max_len by truncating
    and appending a short hash.
    For files, preserve extension if keep_ext is True.
    """
    if max_len <= 0:
        return short_hash(name, 10)

    if len(name) <= max_len:
        return name

    stem = name
    ext = ""
    if keep_ext:
        stem, ext = os.path.splitext(name)

    suffix = "-" + short_hash(name, 8)
    room_for_stem = max_len - len(ext) - len(suffix)

    if room_for_stem < min_base:
        # Try to keep a small visible stem and a smaller hash
        min_stem = max(4, min_base // 2)
        # Leave at least 1 char for stem if possible
        hash_len = max(4, max_len - len(ext) - 1 - min_stem)
        if hash_len < 4:
            # Last resort: hard cut, preserve extension
            return stem[: max_len - len(ext)] + ext
        suffix = "-" + short_hash(name, hash_len)
        room_for_stem = max_len - len(ext) - len(suffix)

    return stem[: max(1, room_for_stem)] + suffix + ext


def path_length(p: Path) -> int:
    # Use resolved absolute path for a conservative count on Windows
    try:
        return len(str(p.resolve()))
    except Exception:
        return len(str(p))


def plan_file_rename(
    root: Path, f: Path, max_name: int, max_total: int
) -> Tuple[Path, Path] | None:
    rel = f.relative_to(root)
    parts = list(rel.parts)
    name = parts[-1]
    new_name = name

    # Enforce segment length
    if len(new_name) > max_name:
        new_name = shorten_segment(new_name, max_name, keep_ext=True)

    candidate = root.joinpath(*parts[:-1], new_name)

    # Enforce total path length (shrink filename further if needed)
    if path_length(candidate) > max_total:
        # Try progressively smaller targets
        cur_len = len(new_name)
        while path_length(candidate) > max_total and cur_len > 12:
            cur_len = max(12, cur_len - 10)
            new_name = shorten_segment(new_name, cur_len, keep_ext=True)
            candidate = root.joinpath(*parts[:-1], new_name)

    if candidate == f:
        return None
    return (f, candidate)


def find_overlong_files(root: Path, files: List[Path], max_total: int) -> List[Path]:
    return [p for p in files if path_length(p) > max_total]


def propose_dir_renames(
    root: Path, dirs: List[Path], max_name: int
) -> Dict[Path, Path]:
    mapping: Dict[Path, Path] = {}
    for d in sorted(dirs, key=lambda x: len(x.parts), reverse=True):
        name = d.name
        if len(name) > max_name:
            new_name = shorten_segment(name, max_name, keep_ext=False)
            if new_name != name:
                mapping[d] = d.with_name(new_name)
    return mapping


def apply_dir_renames(mapping: Dict[Path, Path], apply: bool, verbose: bool) -> int:
    count = 0
    for src in sorted(mapping.keys(), key=lambda p: len(p.parts), reverse=True):
        dst = mapping[src]
        if src == dst:
            continue
        if verbose or not apply:
            print(f"[DIR]  {src} -> {dst}")
        if apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
        count += 1
    return count


def apply_file_renames(
    plans: List[Tuple[Path, Path]], apply: bool, verbose: bool
) -> int:
    count = 0
    # Avoid collisions by adjusting targets if necessary
    final_plans: List[Tuple[Path, Path]] = []
    used_targets: set[Path] = set()

    for src, dst in plans:
        base_dst = dst
        bump = 1
        stem, ext = os.path.splitext(dst.name)
        while (dst in used_targets) or dst.exists():
            suffix = f"-{bump}"
            dst = base_dst.with_name(
                shorten_segment(stem + suffix + ext, DEFAULT_MAX_NAME)
            )
            bump += 1
        used_targets.add(dst)
        final_plans.append((src, dst))

    for src, dst in sorted(final_plans, key=lambda t: len(t[0].parts), reverse=True):
        if src == dst:
            continue
        if verbose or not apply:
            print(f"[FILE] {src} -> {dst}")
        if apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
        count += 1
    return count


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Shorten file and directory names to meet path length limits."
    )
    parser.add_argument("--root", default=".", help="Root directory to scan.")
    parser.add_argument(
        "--max-name",
        type=int,
        default=DEFAULT_MAX_NAME,
        help="Max length for a single path segment.",
    )
    parser.add_argument(
        "--max-total",
        type=int,
        default=DEFAULT_MAX_TOTAL,
        help="Max total path length.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Regex of relative POSIX paths to exclude. Repeatable.",
    )
    parser.add_argument("--apply", action="store_true", help="Apply changes.")
    parser.add_argument(
        "--shorten-dirs",
        action="store_true",
        help="Attempt to shorten directory names.",
    )
    parser.add_argument("--verbose", action="store_true", help="Verbose output.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    excludes = compile_patterns(args.exclude)

    # Collect paths
    all_paths = list(root.rglob("*"))
    files = [
        p
        for p in all_paths
        if p.is_file() and not is_excluded(to_rel(p, root), excludes)
    ]
    dirs = [
        p
        for p in all_paths
        if p.is_dir() and not is_excluded(to_rel(p, root), excludes)
    ]

    # Plan file renames
    file_plans: List[Tuple[Path, Path]] = []
    for f in files:
        plan = plan_file_rename(root, f, args.max_name, args.max_total)
        if plan:
            file_plans.append(plan)

    # Optional directory rename planning
    dir_renames: Dict[Path, Path] = {}
    if args.shorten_dirs:
        dir_renames = propose_dir_renames(root, dirs, args.max_name)

    print(f"Root: {root}")
    print(f"Files scanned: {len(files)}, Dirs scanned: {len(dirs)}")
    print(f"Proposed file renames: {len(file_plans)}")
    if args.shorten_dirs:
        print(f"Proposed dir renames: {len(dir_renames)}")

    # Apply renames
    changed = 0
    if dir_renames:
        changed += apply_dir_renames(
            dir_renames, apply=args.apply, verbose=args.verbose
        )
        # After directory changes, recompute file plans
        all_paths = list(root.rglob("*"))
        files = [
            p
            for p in all_paths
            if p.is_file() and not is_excluded(to_rel(p, root), excludes)
        ]
        file_plans = []
        for f in files:
            plan = plan_file_rename(root, f, args.max_name, args.max_total)
            if plan:
                file_plans.append(plan)

    changed += apply_file_renames(file_plans, apply=args.apply, verbose=args.verbose)

    # Final check
    remaining = find_overlong_files(root, files, args.max_total)
    if remaining:
        print(f"Remaining overlong paths: {len(remaining)}")
        for p in remaining[:20]:
            print(f"  {to_rel(p, root)} ({path_length(p)})")
        if not args.shorten_dirs:
            print("Hint: rerun with --shorten-dirs to reduce directory lengths.")
    else:
        print("All paths within limits.")

    if not args.apply:
        print("Dry run. Use --apply to perform renames.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""Prepare the upstream OpenAPI document for client generation."""

import argparse
import json
from pathlib import Path
from typing import Any


def remove_code_samples(value: Any) -> None:
    if isinstance(value, dict):
        value.pop("x-codeSamples", None)
        for child in value.values():
            remove_code_samples(child)
    elif isinstance(value, list):
        for child in value:
            remove_code_samples(child)


def prepare_spec(input_path: Path, output_path: Path) -> None:
    document = json.loads(input_path.read_text(encoding="utf-8"))
    paths = document.get("paths")
    if not isinstance(paths, dict):
        raise ValueError(f"OpenAPI document has no paths object: {input_path}")

    document["paths"] = {
        path: {"get": path_item["get"]}
        for path, path_item in paths.items()
        if isinstance(path_item, dict) and "get" in path_item
    }
    remove_code_samples(document)
    output_path.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    prepare_spec(args.input, args.output)


if __name__ == "__main__":
    main()

# Releasing (SportradarDatacoreAPI)

## 1) Pre-flight
- Ensure `main` is green in CI
- Confirm version in `pyproject.toml` is updated
- Update changelog/release notes if used

## 2) Tag release
```bash
git checkout main
git pull

git tag vX.Y.Z
git push origin vX.Y.Z
```

## 3) What happens automatically
- GitHub Action `release.yml` verifies tag matches `pyproject.toml` version
- Runs ruff, mypy, and pytest before building
- Builds `sdist` + `wheel` with `uv`
- Publishes to PyPI via trusted publishing
- Artifacts are attached to a GitHub Release for the tag
- GitHub Release notes are auto-generated
- SBOM is generated and build provenance is attested

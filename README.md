# demo-uv-dynamic-versioning

Demonstrating Pythonic [uv](https://docs.astral.sh/uv/) usage with dynamic versioning capabilities from [setuptools-scm](https://github.com/pypa/setuptools-scm).

## Development

1. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/).
1. Install package locally (e.g. `uv pip install -e ".[dev]"`).
1. Run tests (e.g. `uv run poe test`, through [poethepoet](https://poethepoet.natn.io/index.html) task).
1. Build dynamically versioned distribution (e.g. `uv build`).

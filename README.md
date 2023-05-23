# Diacritical

A tool for finding and fixing (TODO) spelling errors in Wikipedia caused by missing diacritics.

## Usage

Install dependencies with poetry:

```bash
$ poetry install
```

Run the tool:

```bash
$ poetry run diacritical
```

Example output:

The tool outputs the word under investigation, followed by the list of potential issues found and the count.

```bash
Kererū:
Flower: https://en.wikipedia.org/wiki/Flower
Panaruawhiti / Endeavour Inlet: https://en.wikipedia.org/wiki/Panaruawhiti_%2F_Endeavour_Inlet
2 articles with potential misspellings found.
```

## Configuration

Config is done using [TOML](https://toml.io/en/) files, in the config directory.

```toml
["Kererū"] # The correct spelling of the misspelled word.
skip = true # Whether to skip processing the word. (optional, default: false)
ignored_patterns = ["Kereru-?Symes", "Count Kereru"] # A list of patterns to ignore. (optional, default: empty list)
ignored_pages = ["Wellington and Manawatu Railway Company"] # A list of pages to ignore. (optional, default: empty list)
```

## Developing

Run the linting and testing tools as follows:

```bash
$ poetry run black --check .
$ poetry run flake8
$ poetry run coverage run --branch -m unittest
$ poetry run coverage report --fail-under 100
```

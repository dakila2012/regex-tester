# regex-tester

A production-ready CLI regex tester that applies user-provided patterns to stdin or input files. It supports key `re` module flags like ignore-case, multiline, dotall, and verbose, with matches highlighted in bold yellow ANSI colors. Handles invalid patterns, missing files, and encoding errors gracefully, providing clean output formatting for quick testing and validation.

## Installation

bash
git clone <repository-url>
cd regex-tester
No external dependencies; uses only Python standard library. Make executable:

bash
chmod +x src/regex_tester.py
Run with `python src/regex_tester.py` or `./src/regex_tester.py`.

## Usage

Show help:

bash
python src/regex_tester.py --help
Test pattern on stdin:

bash
echo "abc 123 def
456 xyz" | python src/regex_tester.py "\d+"
Test pattern on file with ignore-case:

bash
python src/regex_tester.py --ignore-case "hello" input.txt
Other flags: `--multiline` / `-m`, `--dotall` / `-s`, `--verbose` / `-v`, `--version`.

## Features

- Applies regex to stdin (default) or multiple files
- Full support for `re` flags: `IGNORECASE` (`-i`), `MULTILINE` (`-m`), `DOTALL` (`-s`), `VERBOSE` (`-v`)
- Highlights all matches with ANSI bold yellow coloring
- Graceful error handling: invalid regex, file not found, UTF-8 decode errors
- Prints file headers (`=== filename ===`) for multi-file input

## Dependencies

None (Python standard library only: `argparse`, `re`, `sys`).

## Tests

No tests implemented.

## License

MIT
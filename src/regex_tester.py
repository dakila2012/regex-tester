#!/usr/bin/env python3
import argparse
import re
import sys


def highlight_match(match):
    return f"\033[33;1m{match.group(0)}\033[0m"


def main():
    parser = argparse.ArgumentParser(
        description="CLI regex tester that applies user-provided patterns to stdin or files with support for flags like ignore-case and multiline, highlighting matches with ANSI codes."
    )
    parser.add_argument("pattern", help="Regex pattern to test")
    parser.add_argument("files", nargs="*", help="Input files (default: stdin)")
    parser.add_argument(
        "--ignore-case", "-i", action="store_true", help="Ignore case (re.IGNORECASE)"
    )
    parser.add_argument(
        "--multiline", "-m", action="store_true", help="Multiline mode (re.MULTILINE)"
    )
    parser.add_argument(
        "--dotall", "-s", action="store_true", help="Make . match newline (re.DOTALL)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Verbose mode (re.VERBOSE)"
    )
    parser.add_argument("--version", action="version", version="regex-tester 1.0.0")
    args = parser.parse_args()

    flags = 0
    if args.ignore_case:
        flags |= re.IGNORECASE
    if args.multiline:
        flags |= re.MULTILINE
    if args.dotall:
        flags |= re.DOTALL
    if args.verbose:
        flags |= re.VERBOSE

    try:
        regex = re.compile(args.pattern, flags)
    except re.error as e:
        print(
            f"Error: Invalid regex pattern '{args.pattern}': {e}", file=sys.stderr
        )
        sys.exit(2)

    success = False
    if args.files:
        for filename in args.files:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    whole = f.read()
                    subbed = regex.sub(highlight_match, whole)
                    print(f"=== {filename} ===\n{subbed}", end="")
                success = True
            except FileNotFoundError:
                print(f"Error: No such file: {filename}", file=sys.stderr)
                continue
            except UnicodeDecodeError as e:
                print(f"Error: {filename} is not valid UTF-8: {e}", file=sys.stderr)
                continue
            except Exception as e:
                print(f"Error reading {filename}: {e}", file=sys.stderr)
                continue
        if not success:
            sys.exit(1)
    else:
        whole = sys.stdin.read()
        subbed = regex.sub(highlight_match, whole)
        print(subbed, end="")


if __name__ == "__main__":
    main()

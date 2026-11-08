"""Count words, Unicode code points, and lines without dependencies."""
import argparse
import json
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("text", nargs="?", help="Text to analyze; omit to read piped input.")
args = parser.parse_args()
if args.text is None:
    sys.stdin.reconfigure(newline='')
text = args.text if args.text is not None else sys.stdin.read()
print(json.dumps({
    "words": len(text.split()),
    "characters": len(text),
    "lines": len(text.splitlines()),
}, ensure_ascii=True))

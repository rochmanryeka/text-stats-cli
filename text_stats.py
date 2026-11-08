"""Count words, Unicode code points, and lines without dependencies."""
import argparse
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("text", help="Text to analyze; quote text containing spaces.")
args = parser.parse_args()
text = args.text
print(json.dumps({
    "words": len(text.split()),
    "characters": len(text),
    "lines": len(text.splitlines()),
}, ensure_ascii=True))

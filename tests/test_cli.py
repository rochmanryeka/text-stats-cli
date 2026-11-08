"""End-to-end tests for the command-line interface."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "text_stats.py"


class TextStatsTests(unittest.TestCase):
    def test_text_argument_reports_statistics(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "Halo dunia\nPython"],
            capture_output=True, text=True, encoding="utf-8", check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "words": 3, "characters": 17, "lines": 2,
        })

    def test_piped_input_reports_statistics(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], input=b"Halo dunia\nPython",
            capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "words": 3, "characters": 17, "lines": 2,
        })

    def test_empty_and_unicode_inputs(self):
        cases = [
            ("", {"words": 0, "characters": 0, "lines": 0}),
            (" \t ", {"words": 0, "characters": 3, "lines": 1}),
            ("a" + chr(13) + "\nb" + chr(13) + "\n",
             {"words": 2, "characters": 6, "lines": 2}),
            ("a\n", {"words": 1, "characters": 2, "lines": 1}),
            ("\U0001f600 e\u0301", {"words": 2, "characters": 4, "lines": 1}),
        ]
        for text, expected in cases:
            with self.subTest(text=repr(text)):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), text],
                    capture_output=True, text=True, encoding="utf-8", check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout), expected)

    def test_pipe_preserves_crlf_characters(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], input=b"a" + bytes([13, 10]) + b"b" + bytes([13, 10]),
            capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "words": 2, "characters": 6, "lines": 2,
        })

    def test_explicit_empty_argument_takes_priority_over_stdin(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), ""], input="ignored input",
            capture_output=True, text=True, encoding="utf-8", check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "words": 0, "characters": 0, "lines": 0,
        })

    def test_empty_pipe_reports_zero_counts(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], input="",
            capture_output=True, text=True, encoding="utf-8", check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {
            "words": 0, "characters": 0, "lines": 0,
        })


if __name__ == "__main__":
    unittest.main()

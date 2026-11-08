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


if __name__ == "__main__":
    unittest.main()

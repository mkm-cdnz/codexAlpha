from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "hermes" / "scripts" / "validate_poc.py"
SPEC = importlib.util.spec_from_file_location("validate_poc", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ValidatePocTests(unittest.TestCase):
    def test_repository_skills_validate(self):
        result = MODULE.validate(ROOT / "hermes")
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(set(MODULE.SKILLS), set(result["manifest"]))

    def test_install_is_non_destructive_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            installed = MODULE.install(ROOT / "hermes", home, force=False)
            self.assertEqual(4, len(installed))
            with self.assertRaises(FileExistsError):
                MODULE.install(ROOT / "hermes", home, force=False)


if __name__ == "__main__":
    unittest.main()

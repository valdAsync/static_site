import unittest

from getcontent import extract_title


class TestGetContent(unittest.TestCase):
    def test_extract_title(self):
        content = "# Hello, world!"
        self.assertEqual(
            extract_title(content),
            "Hello, world!",
        )

        content = "# Hello, world!   "
        self.assertEqual(
            extract_title(content),
            "Hello, world!",
        )

        content = "#      Hello, world!   "
        self.assertEqual(
            extract_title(content),
            "Hello, world!",
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from generate_pages import extract_title

class TestTitleExtract(unittest.TestCase):
    def test_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

if __name__ == "__main__":
    unittest.main()
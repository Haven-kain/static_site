import unittest

from generate_pages import extract_title

class TestTitleExtract(unittest.TestCase):
    def test_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_extra_text(self):
        md = """
The title

Will **be**

### maybe
## Somewhere


# in the text

_possibly_

"""
        title = extract_title(md)
        self.assertEqual(title, "in the text")
        
if __name__ == "__main__":
    unittest.main()
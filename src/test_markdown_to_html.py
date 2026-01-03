import unittest

from markdown_to_html import markdown_to_html

class TestMdToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is.

A simple paragraph.


of markdown.
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><p>This is.</p><p>A simple paragraph.</p><p>of markdown.</p></div>"
        )

    def test_heading(self):
        pass

    def test_code(self):
        pass

    def test_quote(self):
        pass

    def test_ul(self):
        pass

    def test_ol(self):
        pass
    

if __name__ == "__main__":
    unittest.main()
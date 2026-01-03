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
        md = """
# This is.

## Markdown.

### With multiple.

###### Headings.

####### and a paragraph.
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is.</h1><h2>Markdown.</h2><h3>With multiple.</h3><h6>Headings.</h6><p>####### and a paragraph.</p></div>"
        )

    def test_code(self):
        md = """
This is a paragraph.

```
This is a.
    code block.


With extra.
    new lines.
        and indentation.

return
```

This is another paragraph.
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a paragraph.</p><pre><code>```This is a.\n    code block.\n\n\nWith extra.\n    new lines.\n        and indentation.\n\nreturn```</code></pre><p>This is another paragraph.</p></div>"
        )

    def test_quote(self):
        pass

    def test_ul(self):
        pass

    def test_ol(self):
        pass


if __name__ == "__main__":
    unittest.main()
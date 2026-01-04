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
            "<div><p>This is a paragraph.</p><pre><code>This is a.\n    code block.\n\n\nWith extra.\n    new lines.\n        and indentation.\n\nreturn\n</code></pre><p>This is another paragraph.</p></div>"
        )

    def test_quote(self):
        md = """
>This is a quote
>block

With a paragraph.

> in between

> more quotes.
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\nblock</blockquote><p>With a paragraph.</p><blockquote>in between</blockquote><blockquote>more quotes.</blockquote></div>"
        )

    def test_ul(self):
        md = """
This is a.

- Unordered list
- With
- Extra list items

-and a paragraph

- Followed by

- Another unordered list.
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a.</p><ul><li>Unordered list\n</li><li>With\n</li><li>Extra list items</li></ul><p>-and a paragraph</p><ul><li>Followed by</li></ul><ul><li>Another unordered list.</li></ul></div>"
        )

    def test_ol(self):
        md = """
This is a.

1. Ordered list
2. With
3. some list
4. items

followed by a paragraph

1. and another
2. ordered list
"""

        nodes = markdown_to_html(md)
        html = nodes.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a.</p><ol><li>Ordered list</li><li>With</li><li>some list</li><li>items</li></ol><p>followed by a paragraph</p><ol><li>and another</li><li>ordered list</li></ol></div>"
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


if __name__ == "__main__":
    unittest.main()
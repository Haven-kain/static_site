import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_block_split(self):
        md = """
This is a paragraph
of text.

With.

More paragraph blocks.
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph\nof text.",
                "With.",
                "More paragraph blocks."
            ]
        )

    def test_code_split(self):
        md = """
This is a paragraph.

```
With
    nested indentation


    and extra new lines
that

    various white space.



```

and extra text.
at the end of the md.

"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph.",
                "```With\n    nested indentation\n\n\n    and extra new lines\nthat\n\n    various white space.```",
                "and extra text.\nat the end of the md."
            ]
        )

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        pass

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

    def test_mixed(self):
        pass

if __name__ == "__main__":
    unittest.main()
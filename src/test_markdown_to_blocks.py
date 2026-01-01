import unittest

from markdown_blocks import markdown_to_blocks, block_to_blocktype, BlockType

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
        md = "This is normal text"
        block_type = block_to_blocktype(md)
        self.assertEqual(
            block_type,
            BlockType.PARAGRAPH
        )

    def test_heading(self):
        h1 = block_to_blocktype("# heading")
        h2 = block_to_blocktype("## heading")
        h3 = block_to_blocktype("### heading")
        h4 = block_to_blocktype("#### heading")
        h5 = block_to_blocktype("##### heading")
        h6 = block_to_blocktype("###### heading")
        paragraph = block_to_blocktype("####### heading")
        h_paragraph = block_to_blocktype("#heading")
        self.assertEqual(
            paragraph,
            BlockType.PARAGRAPH
            )
        self.assertEqual(
            h_paragraph,
            BlockType.PARAGRAPH
        )
        self.assertEqual(h1, BlockType.HEADING)
        self.assertEqual(h2, BlockType.HEADING)
        self.assertEqual(h3, BlockType.HEADING)
        self.assertEqual(h4, BlockType.HEADING)
        self.assertEqual(h5, BlockType.HEADING)
        self.assertEqual(h6, BlockType.HEADING)

    def test_code(self):
        block = """
```
this is a


    code
block
```
"""
        code = block_to_blocktype(block)
        self.assertEqual(code, BlockType.CODE)

    def test_quote(self):
        quote_block = ">Quote\n>Block\n> With\n> different spacing"
        quote = block_to_blocktype(quote_block)
        self.assertEqual(quote, BlockType.QUOTE)

    def test_ul(self):
        ul_block = "- This is a\n- unordered\n- list"
        ul = block_to_blocktype(ul_block)
        self.assertEqual(ul, BlockType.UL)

    def test_ol(self):
        ol_block = "1. This is\n2. an\n3. Ordered\n4. list"
        ol = block_to_blocktype(ol_block)
        self.assertEqual(ol, BlockType.OL)

if __name__ == "__main__":
    unittest.main()
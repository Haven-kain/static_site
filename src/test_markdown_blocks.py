import unittest

from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks(self):
        md = """






"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_lots_of_new_lines(self):
        md = """


This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block_type(self):
        text = "#heading"
        other_text = "####### heading"
        h1 = "# heading"

        text_block = markdown_to_blocks(text)
        text_block_type = block_to_block_type(text_block[0])

        other_text = markdown_to_blocks(other_text)
        other_text = block_to_block_type(other_text[0])

        h1_block = markdown_to_blocks(h1)
        h1_type = block_to_block_type(h1_block[0])

        self.assertEqual(text_block_type, BlockType.PARAGRAPH)
        self.assertEqual(other_text, BlockType.PARAGRAPH)
        self.assertEqual(h1_type, BlockType.HEADING)

    def test_code_block_type(self):
        code = """
        ```
        this is code
        ```
        """
        not_code = "```this is not code"

        code = markdown_to_blocks(code)
        code = block_to_block_type(code[0])

        not_code = markdown_to_blocks(not_code)
        not_code = block_to_block_type(not_code[0])

        self.assertEqual(code, BlockType.CODE)
        self.assertEqual(not_code, BlockType.PARAGRAPH)

    def test_quote_block(self):
        quote = ">This is a quote"
        another_quote = "> This is another quote"
        not_a_quote = "This is not a quote >"

        quote = markdown_to_blocks(quote)
        another_quote = markdown_to_blocks(another_quote)
        not_a_quote = markdown_to_blocks(not_a_quote)



if __name__ == "__main__":
    unittest.main()
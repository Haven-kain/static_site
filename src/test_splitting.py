import unittest

from splitting_functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplittingFuncs(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_bold(self):
        node = TextNode("This is text with a *bold* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_italic(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ]
        )

    def test_missing_delim(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        node2 = TextNode("This is text with a code block` word", TextType.TEXT)
        node3 = TextNode("This is text with a italic_ word", TextType.TEXT)
        node4 = TextNode("This is text with a _italic word", TextType.TEXT)
        node5 = TextNode("This is text with a bold* word", TextType.TEXT)
        node6 = TextNode("This is text with a *bold word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
            split_nodes_delimiter([node2], "`", TextType.CODE)
            split_nodes_delimiter([node3], "_", TextType.ITALIC)
            split_nodes_delimiter([node4], "_", TextType.ITALIC)
            split_nodes_delimiter([node5], "*", TextType.BOLD)
            split_nodes_delimiter([node6], "*", TextType.BOLD)

class TestExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()
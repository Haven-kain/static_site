import unittest

from splitting_functions import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitFunctions(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
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

    def test_code(self):
        node = TextNode("This is text with a `code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ]
        )
        
    def test_non_matching(self):
        node = TextNode("This is text with a **bold word", TextType.TEXT)
        node2 = TextNode("** This is text", TextType.TEXT)
        node3 = TextNode("This is text **", TextType.TEXT)
        with self.assertRaises(Exception) as err:
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            new_node2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
            new_nodes3 = split_nodes_delimiter([node3], "**", TextType.BOLD)

            self.assertEqual(str(err), "Invalid Markdown Syntax: Missing Matching Delimiter")

    def test_bold_node(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a _italic_ word", TextType.TEXT)
        node_list = [node, node2]
        new_nodes = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a bold node", TextType.BOLD),
                TextNode("This is a " , TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()
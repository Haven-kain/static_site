import unittest

from splitting_functions import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnode,
)

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
        node = TextNode("This is a **bold** node", TextType.BOLD)
        node2 = TextNode("This is a _italic_ word", TextType.TEXT)
        node_list = [node, node2]
        new_nodes = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a **bold** node", TextType.BOLD),
                TextNode("This is a " , TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        self.assertEqual(
            extracted,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

    def test_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_links(text)
        self.assertEqual(
            extracted,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_link_with_following_text(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
            ]
        )

    def test_image_with_following_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another", TextType.TEXT),
            ]
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        split_text = text_to_textnode(text)
        self.assertEqual(
            split_text,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_text_to_textnode(self):
        text = "This is _text_ with an **italic** word and a ![code block](https://i.imgur.com/fJRm4Vk.jpeg) and an `obi wan image` and a [link](https://boot.dev)"
        split_text = text_to_textnode(text)
        self.assertEqual(
            split_text,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.ITALIC),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.BOLD),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.CODE),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", [LeafNode(None, "Normal text")])
        node2 = ParentNode("p", [LeafNode(None, "Normal text")])
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", 
                         node.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_family_tree(self):
        grandchild_node = LeafNode("b", "Grandchild Node")
        nephew_node = LeafNode(None, "Nephew Node")
        child_node = ParentNode("span", [grandchild_node, LeafNode(None, "Normal text"), LeafNode("i", "italic text"),])
        cousin_node = ParentNode("p", [LeafNode("b", "Bold text"), nephew_node])
        uncle_node = ParentNode("p", [cousin_node])
        parent_node = ParentNode("div", [child_node, uncle_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>Grandchild Node</b>Normal text<i>italic text</i></span><p><p><b>Bold text</b>Nephew Node</p></p></div>",
            )

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()

if __name__ == "__main__":
    unittest.main()
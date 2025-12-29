import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_html(self):
        node = HTMLNode(value="This is a node")
        self.assertEqual("This is a node", node.value)

    def test_empty(self):
        node = HTMLNode()
        self.assertEqual(None, node.tag)
        self.assertEqual(None, node.value)
        self.assertEqual(None, node.children)
        self.assertEqual(None, node.props)

    def test_props(self):
        node = HTMLNode(props={
    "href": "https://www.google.com",
    "target": "_blank",
})      
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
            )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
            )
        
    def test_b_tag(self):
        node = LeafNode("b", "No way!")
        self.assertEqual(
            node.to_html(),
            "<b>No way!</b>"
        )

    def test_no_tag(self):
        node = LeafNode(None, "This is a node")
        self.assertEqual(node.to_html(), "This is a node")

    def test_error(self):
        with self.assertRaises(Exception):
            LeafNode(None)

class TestParentNode(unittest.TestCase):
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

    def test_multiple_children(self):
        child_node = LeafNode("span", "child")
        sister_node = LeafNode("b", "sister")
        brother_node = LeafNode("p", "brother")
        children = [child_node, sister_node, brother_node]
        parent_node = ParentNode("div", children)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><b>sister</b><p>brother</p></div>"
                         )

    def test_no_children(self):
        with self.assertRaises(Exception):
            ParentNode("p")

if __name__ == "__main__":
    unittest.main()
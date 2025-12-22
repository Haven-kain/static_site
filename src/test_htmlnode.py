import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_none(self):
        node = HTMLNode()
        self.assertEqual(None, node.tag)
        self.assertEqual(None, node.value)
        self.assertEqual(None, node.props)
        self.assertEqual(None, node.children)

    def test_empty_props_to_html(self):
        node = HTMLNode()
        node2 = HTMLNode(props="")
        node3 = HTMLNode(props={})
        self.assertEqual("", node.props_to_html())
        self.assertEqual("", node2.props_to_html())
        self.assertEqual("", node3.props_to_html())

    def test_values(self):
        child_node = HTMLNode()
        node = HTMLNode("p", "This is a html node", child_node, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual("p", node.tag)
        self.assertEqual("This is a html node", node.value)
        self.assertEqual(HTMLNode(), child_node)
        self.assertEqual({"href": "https://www.google.com", "target": "_blank"}, node.props)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        prop_string = node.props_to_html()
        self.assertEqual(' href="https://www.google.com" target="_blank"', prop_string)

    def test_repr(self):
        child_node = HTMLNode()
        node = HTMLNode("p", "This is a html node", child_node, {"href": "https://www.google.com", "target": "_blank"})
        node_str = node.__repr__()
        self.assertEqual("HTMLNode(p, This is a html node, HTMLNode(None, None, None, None), {'href': 'https://www.google.com', 'target': '_blank'})", node_str)

if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
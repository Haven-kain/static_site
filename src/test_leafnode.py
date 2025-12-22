import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag=None,value="This is a leaf node")
        node2 = LeafNode(tag=None, value="This is a leaf node")
        self.assertEqual(node, node2)

    def test_empty_value(self):
        with self.assertRaises(TypeError):
            LeafNode(tag=None)
        with self.assertRaises(TypeError):
            LeafNode(tag=None).to_html()

    def test_to_html(self):
        node = LeafNode("p", "This is a text leaf node")
        self.assertEqual("<p>This is a text leaf node</p>", node.to_html())

    def test_none_tag(self):
        node = LeafNode(tag=None, value="This is a leaf node")
        self.assertEqual("This is a leaf node", node.to_html())

if __name__ == "__main__":
    unittest.main()
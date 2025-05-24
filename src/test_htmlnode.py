import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    #Base Nodes
    def test_props_to_html(self):
        node = HTMLNode("p", "text", None, None)
        node2 = HTMLNode("a", "link", None, {"href": "https://www.boot.dev"})
        node3 = HTMLNode("h1", "My Title", None, {})
        node4 = HTMLNode("h1", "test", None, {"href": "https://www.boot.dev", "target": "_blank"})

        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), " href=\"https://www.boot.dev\"")
        self.assertEqual(node3.props_to_html(), "")
        self.assertEqual(node4.props_to_html(), " href=\"https://www.boot.dev\" target=\"_blank\"")

    #Leaf Nodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a test")
        self.assertEqual(node.to_html(), "This is a test")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    #Parent nodes
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
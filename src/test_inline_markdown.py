import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_code_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])
        
    def test_text_emptyCode_text(self):
        node = TextNode("text `` more text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("text ", TextType.TEXT),
            TextNode(" more text", TextType.TEXT),
            ])
        
    def test_emptyCode_text_emptyCode(self):
        node = TextNode("``text block``", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("text block", TextType.TEXT)
            ])

if __name__ == "__main__":
    unittest.main()
import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.HEADING)

    def test_code_block(self):
        block = "```\nCode block\n```"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.CODE)

    def test_quote_block(self):
        block = "> First line " \
        "> Second line"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Apple" \
        "- Bear" \
        "- Carrot"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First" \
        "2. Second" \
        "3. Third"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is just a normal block of text. It doesn't start with any special markdown syntax."
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.PARAGRAPH)

    def test_mixed_block(self):
        block = "- Apple\nNot a list\n- Carrot"
        new_block = block_to_block_type(block)
        self.assertNotEqual(new_block, BlockType.UNORDERED_LIST)
        self.assertEqual(new_block, BlockType.PARAGRAPH)

class BlockToHTML(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )
        
    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
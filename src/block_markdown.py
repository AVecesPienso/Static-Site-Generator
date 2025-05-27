from enum import Enum
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        spaces = block.strip()
        if spaces != "":
            new_blocks.append(spaces)
    return new_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    for i in range(1, 7):
        prefix = "#" * i + " "
        if block.startswith(prefix):
            return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    final_list = []
    for block in block_list:
        block_type = block_to_block_type(block)
        if block_type != BlockType.CODE:
            rblock = block.replace("\n", " ")
            block_tag = block_type_to_html_tag(block_type, rblock)
            text_node = text_to_textnodes(rblock)
            children_node_list = []
            for node in text_node:
                html_nodes = text_node_to_html_node(node)
                children_node_list.append(html_nodes)
            html_nodes = ParentNode(block_tag, children_node_list)
            final_list.append(html_nodes)
        else:
            code_node = TextNode(block, block_type)
            html_code = [text_node_to_html_node(code_node)]
            nested_code = ParentNode("pre", html_code)
            final_list.append(nested_code)
    div_node = ParentNode("div", final_list)
    return div_node


def block_type_to_html_tag(block_type, block=None):
    if block_type == BlockType.QUOTE:
        return "blockquote"
    if block_type == BlockType.UNORDERED_LIST:
        return "ul"
    if block_type == BlockType.ORDERED_LIST:
        return "ol"
    if block_type == BlockType.PARAGRAPH:
        return "p"
    if block_type == BlockType.HEADING:
        if block.startswith("# "):
            return "h1"
        if block.startswith("## "):
            return "h2"
        if block.startswith("### "):
            return "h3"
        if block.startswith("#### "):
            return "h4"
        if block.startswith("##### "):
            return "h5"
        if block.startswith("###### "):
            return "h6"
from enum import Enum

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



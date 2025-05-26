def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        spaces = block.strip()
        if spaces != "":
            new_blocks.append(spaces)
    return new_blocks


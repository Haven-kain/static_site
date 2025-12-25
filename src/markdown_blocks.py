def markdown_to_blocks(markdown):
    blocks = markdown.strip("\n")
    blocks = blocks.split("\n\n")
    for block in blocks:
        if block == "":
            del block
    return blocks
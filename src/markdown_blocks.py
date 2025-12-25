from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "ul",
    ORDERED_LIST = "ol",

def markdown_to_blocks(markdown):
    blocks = markdown.strip()
    blocks = blocks.split("\n\n")
    for block in blocks:
        if block == "":
            blocks.remove(block)
    return blocks

def block_to_block_type(block):
    block = block[0]
    if len(block.split("# ")[0]) > 5:
        return BlockType.PARAGRAPH
    
    if len(block.split("# ")) == 2:
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        return BlockType.QUOTE
    
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
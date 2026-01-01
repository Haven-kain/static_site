from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UL = "unordered list",
    OL = "ordered list"


def markdown_to_blocks(markdown):
    code_split = markdown.strip().split("```")
    if len(code_split) != 2:
        blocks = []
        for i in range(len(code_split)):
            if i % 2 != 0:
                blocks.append("```" + code_split[i].strip() + "```")
                continue
            blocks.extend([block.strip() for block in code_split[i].split("\n\n") if block.strip() != ""])
        return blocks

    blocks = [block.strip() for block in markdown.split("\n\n") if block.strip() != ""]
    return blocks

def block_to_blocktype(block):
    block = block.strip()
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```") and block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UL
    elif block.startswith("1. "):
        line_count = 1
        for line in lines:
            if not line.startswith(f"{line_count}. "):
                return BlockType.PARAGRAPH
            line_count += 1
        return BlockType.OL
    
    return BlockType.PARAGRAPH
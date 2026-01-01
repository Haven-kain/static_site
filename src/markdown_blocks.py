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
                blocks.append(code_split[i].strip())
                continue
            blocks.extend([block.strip() for block in code_split[i].split("\n\n") if block.strip() != ""])
        return blocks

    blocks = [block.strip() for block in markdown.split("\n\n") if block.strip() != ""]
    return blocks

def block_to_blocktype(block):
    pass
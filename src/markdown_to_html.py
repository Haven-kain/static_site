from markdown_blocks import markdown_to_blocks, BlockType, block_to_blocktype
from textnode import text_node_to_html_node
from htmlnode import ParentNode

def markdown_to_html(markdown):
    html = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.PARAGRAPH:
            pass
        elif block_type == BlockType.HEADING:
            pass
        elif block_type == BlockType.CODE:
            pass
        elif block_type == BlockType.QUOTE:
            pass
        elif block_type == BlockType.UL:
            pass
        elif block_type == BlockType.OL:
            pass
    return ParentNode("div", html)

def paragraph_to_html(block):
    pass

def heading_to_html(block):
    pass

def code_to_html(block):
    pass

def quote_to_html(block):
    pass

def ul_to_html(block):
    pass

def ol_to_html(block):
    pass

def text_to_children(text):
    pass
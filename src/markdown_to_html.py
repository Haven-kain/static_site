from markdown_blocks import markdown_to_blocks, BlockType, block_to_blocktype
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode
from splitting_functions import text_to_textnodes

def markdown_to_html(markdown):
    html = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.PARAGRAPH:
            html.append(paragraph_to_html(block))
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
    children = text_to_children(block)
    return ParentNode("p", children)

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
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children
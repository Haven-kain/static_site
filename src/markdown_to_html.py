from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                pass
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass

def text_to_children(text):
    pass

def heading_to_html(text):
    pass

def code_to_html(text):
    pass
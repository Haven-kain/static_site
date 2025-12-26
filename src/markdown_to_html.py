from htmlnode import ParentNode, HTMLNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from splitting_functions import text_to_textnode
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in blocks:
        html_children.append(block_to_html_node(block))
    return wrap_blocks_in_div(html_children)

def wrap_blocks_in_div(block_nodes):
    return ParentNode("div", block_nodes)

def block_to_html_node(block):
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            return paragraph_to_html(block)
        case BlockType.HEADING:
            return heading_to_html(block)
        case BlockType.CODE:
            return code_to_html(block)
        case BlockType.QUOTE:
            return quote_to_html(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html(block)

def paragraph_to_html(text):
    lines = [ln.strip() for ln in text.split("\n") if ln.strip() != ""]
    cleaned_lines = " ".join(lines)
    children = text_to_children(cleaned_lines)
    return ParentNode("p", children)

def heading_to_html(text):
    split_text = text.split("# ")
    h_count = len(split_text[0]) + 1
    children = text_to_children(text)
    return ParentNode(f"h{h_count}", children)

def code_to_html(text):
    lines = text.strip("```")
    lines = [(ln.strip() + "\n") for ln in lines.split("\n") if ln.strip() != ""]
    lines = "".join(lines)
    code_node = TextNode(lines, TextType.CODE)
    html_node = text_node_to_html_node(code_node)
    return ParentNode("pre", [html_node])

def quote_to_html(text):
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def unordered_list_to_html(text):
     children = text_to_children(text)
     for child in children:
        child.tag = "li"
     return ParentNode("ul", children)

def ordered_list_to_html(text):
    children = text_to_children(text)
    for child in children:
        child.tag = "li"
    return ParentNode("ol", children)

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
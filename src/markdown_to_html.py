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
            html.append(heading_to_html(block))
        elif block_type == BlockType.CODE:
            html.append(code_to_html(block))
        elif block_type == BlockType.QUOTE:
            html.append(quote_to_html(block))
        elif block_type == BlockType.UL:
            html.append(ul_to_html(block))
        elif block_type == BlockType.OL:
            html.append(ol_to_html(block))
    return ParentNode("div", html)

def paragraph_to_html(block):
    lines = [line.strip() for line in block.split("\n")]
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html(block):
    block = block.split("# ")
    count = len(block[0]) + 1
    children = text_to_children(block[1])
    return ParentNode(f"h{count}", children)

def code_to_html(block):
    block = block.strip("```") + "\n"
    node = TextNode(block, TextType.CODE)
    node = text_node_to_html_node(node)
    return ParentNode("pre", [node])

def quote_to_html(block):
    children = []
    lines = [line .lstrip() for line in block.split(">")]
    for line in lines:
        children.extend(text_to_children(line))
    return ParentNode("blockquote", children)

def ul_to_html(block):
    children = []
    lines = [line.lstrip() for line in block.split("- ")]
    for line in lines:
        children.extend(text_to_children(line))

    for child in children:
        child.tag = "li"
    return ParentNode("ul", children)

def ol_to_html(block):
    children = text_to_children(block)
    children = []
    lines = [line.strip() for line in block.split("\n")]
    line_count = 1
    for line in lines:
        line = line.strip(f"{line_count}. ")
        children.extend(text_to_children(line))
        line_count += 1

    for child in children:
        child.tag = "li"
    return ParentNode("ol", children)

def text_to_children(text):
    children = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children
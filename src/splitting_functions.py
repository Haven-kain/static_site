import re

from textnode import TextNode, TextType

"""
Functionality to add later:
-Recursive checking of delimiters
-Dynamic checking of delimiters
"""

def split_nodes_delimiter(old_node, delimiter, text_type):
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Invalid Markdown Syntax: Missing Matching Delimiter")
        
        for i in range(len(split_node)):
            if i % 2 != 0:
                new_nodes.append(TextNode(split_node[i], text_type))
                continue
            new_nodes.append(TextNode(split_node[i], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
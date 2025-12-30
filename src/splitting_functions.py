import re

from textnode import TextNode, TextType

def split_nested_nodes(old_node, delimiter, text_type):
    new_nodes = []
    for node in old_node:
        
        if "`" in node.text:
            return split_nodes_delimiter([node], delimiter, text_type)
        
        split_nodes = split_nodes_delimiter([node], delimiter, text_type)

        for i in range(len(split_nodes)):
            current_node = split_nodes[i]
            starting_char = current_node.text[0]
            ending_char = current_node.text[-1]

            if starting_char != ending_char:
                continue

            match starting_char and ending_char:
                case "*":
                    node = split_nodes_delimiter([node], "*", TextType.BOLD)
                    split_nodes[i] = TextNode(node[1], current_node.text_type)
                case "_":
                    node = split_nodes_delimiter([node], "_", TextType.ITALIC)
                    split_nodes[i] = TextNode(node[1], current_node.text_type)
                case _:
                    continue
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_delimiter(old_node, delimiter, text_type):    
    new_nodes = []
    for node in old_node:

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
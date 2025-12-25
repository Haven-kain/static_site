from textnode import TextNode, TextType

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
            continue

        split_node = node.text.split(delimiter)

        if len(split_node) % 3 != 0:
            raise Exception("Invalid Markdown Syntax: Missing Matching Delimiter")
        
        for i in range(len(split_node)):
            if i % 2 != 0:
                new_nodes.append(TextNode(split_node[i], text_type))
                continue

            new_nodes.append(TextNode(split_node[i], TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    extracted = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return extracted

def extract_markdown_links(text):
    extracted = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return extracted

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_images(node.text)
        split_nodes = re.split(r"\!(.*?)\)", node.text)
        link_counter = 0

        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
                continue
            
            new_nodes.append(TextNode(extracted[link_counter][0], TextType.IMAGE, extracted[link_counter][1]))
            link_counter += 1
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_links(node.text)
        split_nodes = re.split(r"\[(.*?)\)", node.text)
        link_counter = 0

        for i in range(len(split_nodes)):
            if split_nodes[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
                continue
            
            new_nodes.append(TextNode(extracted[link_counter][0], TextType.LINK, extracted[link_counter][1]))
            link_counter += 1
    
    return new_nodes

def text_to_textnode(text):
    text_node = TextNode(text, TextType.TEXT)
    split_nodes = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    split_nodes = split_nodes_delimiter(split_nodes, "_", TextType.ITALIC)
    split_nodes = split_nodes_delimiter(split_nodes, "`", TextType.CODE)
    split_nodes = split_nodes_image(split_nodes)
    split_nodes = split_nodes_link(split_nodes)

    return split_nodes
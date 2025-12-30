from textnode import TextNode, TextType

def split_nodes_delimiter(old_node, delimiter, text_type):
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_node = node.split(delimiter)
        if len(split_node) %2 == 0:
            raise Exception("Invalid Markdown Syntax: Missing Matching Delimiter")
        
        for node in split_node:
            if not node.strip():
                new_nodes.append(TextNode(node, text_type))
                continue
            new_nodes.append(TextNode(node, TextType.TEXT))
    return new_nodes
            
from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_italic,
    text_type_text,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown syntax: mismatched delimiters")
        for i, part in enumerate(parts):
            if part:
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, text_type_text))
                else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes


node = TextNode("This is text with a **bolded word** and **another**", text_type_text)
new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

print(new_nodes)

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode


def main():
    text_node = TextNode("hello", "text", "https://www.google.com")
    print(text_node)
    print("#########################")

    html_node = HTMLNode(
        "div", "hello", [text_node], {"href": "https://www.google.com"}
    )
    print(html_node)
    print(html_node.props_to_html())

    print("#########################")

    leaf_node = LeafNode("p", "This is a paragraph of text.")
    print(leaf_node.to_html())
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())


main()

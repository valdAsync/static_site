from htmlnode import HTMLNode
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


main()

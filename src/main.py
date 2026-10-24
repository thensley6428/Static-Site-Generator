from textnode import TextNode, TextType

def main():
    node = TextNode("hello", TextType.BOLD, "https://thisisalink.com")
    print(node)

main()
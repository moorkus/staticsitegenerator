import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is also a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD, "url.com")

        #print(f"Test {node} == {node2}")
        self.assertEqual(node, node2)

        #print(f"Test {node} != {node3}")
        self.assertNotEqual(node, node3)

        #print(f"Test {node} != {node4}")
        self.assertNotEqual(node, node4)

        #print(f"Test {node} != {node5}")
        self.assertNotEqual(node, node5)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.ITALIC, "url.com")
        
        #print(f"Test str(node) == TextNode(This is a text node, bold text, None)")
        self.assertEqual(str(node), "TextNode(This is a text node, bold text, None)")

        #print(f"Test str(node2) == TextNode(This is also a text node, italic text, url.com)")
        self.assertEqual(str(node2), "TextNode(This is also a text node, italic text, url.com)")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
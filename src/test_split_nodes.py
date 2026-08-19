import unittest
from textnode import *
from split_nodes import *

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected_split_node = [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("code block", TextType.CODE),
                                TextNode(" word", TextType.TEXT),
                                ]

        #print(f"Test split_nodes_delimiter([{node}], \"`\", TextType.CODE)=={expected_split_node}")
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected_split_node)

        node = TextNode("This is text with a **BOLD** word", TextType.TEXT)
        expected_split_node = [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("BOLD", TextType.BOLD),
                                TextNode(" word", TextType.TEXT),
                                ]

        #print(f"Test split_nodes_delimiter([{node}], \"**\", TextType.BOLD)=={expected_split_node}")
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected_split_node)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =             [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ]
        #print(f"Test split_images({node})=={expected}")
        #print(f"NEW NODES = {new_nodes}")
        self.assertListEqual(
            new_nodes,
            expected
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        #print(f"Test text_to_textnodes({text})=={expected}")
        self.assertListEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
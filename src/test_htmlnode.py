import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Lalala test", None, {"href": "https://www.google.com","target": "_blank",})
        expected_props_to_html_node = " href=\"https://www.google.com\" target=\"_blank\""

        node2= HTMLNode("a", "Lalala re test", [node], {"href": "https://aaaaaa.fr","target": "salu",})
        expected_props_to_html_node2 = " href=\"https://aaaaaa.fr\" target=\"salu\""

        #print(f"Test {node}.props_to_html=={expected_props_to_html_node}")
        self.assertEqual(node.props_to_html(), expected_props_to_html_node)

        #print(f"Test {node2}.props_to_html=={expected_props_to_html_node2}")
        self.assertEqual(node2.props_to_html(), expected_props_to_html_node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected_to_html_node = "<p>Hello, world!</p>"

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_to_html_node2 = "<a href=\"https://www.google.com\">Click me!</a>"

        node3 = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        expected_to_html_node3 = "Click me!"

        node4 = LeafNode("a", None, {"href": "https://www.google.com"})
        expected_to_html_node4 = "value missing"

        #print(f"Test {node}.to_html=={expected_to_html_node}")
        self.assertEqual(node.to_html(), expected_to_html_node)

        #print(f"Test {node2}.to_html=={expected_to_html_node2}")
        self.assertEqual(node2.to_html(), expected_to_html_node2)

        #print(f"Test {node3}.to_html=={expected_to_html_node3}")
        self.assertEqual(node3.to_html(), expected_to_html_node3)

        with self.assertRaises(ValueError, msg=expected_to_html_node4) as cm:
            #print(f"Test {node4}.to_html -> Value Error : {expected_to_html_node4}")
            print(node4.to_html())
        self.assertEqual(str(cm.exception), expected_to_html_node4)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        expected_to_html_parent_node = "<div><span>child</span></div>"
        #print(f"Test {parent_node}.to_html=={expected_to_html_parent_node}")
        self.assertEqual(parent_node.to_html(), expected_to_html_parent_node)


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        expected_to_html_parent_node = "<div><span><b>grandchild</b></span></div>"
        #print(f"Test {parent_node}.to_html=={expected_to_html_parent_node}")
        self.assertEqual(
            parent_node.to_html(),
            expected_to_html_parent_node,
        )

  
    

if __name__ == "__main__":
    unittest.main()
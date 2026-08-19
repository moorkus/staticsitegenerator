import unittest
from blocks import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ]
        blocks = markdown_to_blocks(md)
        #print(f"Test markdown_to_blocks({md})=={expected}")
        self.assertEqual(blocks, expected)

    def test_block_to_block_type(self):
        md = "# lalala"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = "## lalala"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = "###eee"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = "####"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = "##### "
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = "###### dddd"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = "####### jkfdji"
        expected = BlockType.HEADING
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = """```
```"""
        expected = BlockType.CODE
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = """```
lalala le code
```"""
        expected = BlockType.CODE
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = "```"
        expected = BlockType.CODE
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected) 

        md = """>hiujdhuifhiu
> ojdaojzoda"""
        expected = BlockType.QUOTE
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = """>hiujdhuifhiu
ojdaojzoda"""
        expected = BlockType.QUOTE
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = """- hiujdhuifhiu
- ojdaojzoda"""
        expected = BlockType.UNORDERED_LIST
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = """-hiujdhuifhiu
- ojdaojzoda"""
        expected = BlockType.UNORDERED_LIST
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = """1. hiujdhuifhiu
2. ojdaojzoda"""
        expected = BlockType.ORDERED_LIST
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)

        md = """3. hiujdhuifhiu
4. ojdaojzoda"""
        expected = BlockType.ORDERED_LIST
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})!={expected}")
        self.assertNotEqual(res, expected)

        md = "lulululu salu"
        expected = BlockType.PARAGRAPH
        res = block_to_block_type(md)
        #print(f"Test block_to_block_type({md})=={expected}")
        self.assertEqual(res, expected)


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )      

if __name__ == "__main__":
    unittest.main()
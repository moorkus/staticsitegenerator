import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        test_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        matches = extract_markdown_images(test_text)
        #print(f"Test extract_markdown_images({test_text})=={expected}")
        self.assertListEqual(matches, expected)

        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = []
        matches = extract_markdown_images(test_text)
        #print(f"Test extract_markdown_images({test_text})=={expected}")
        self.assertListEqual(matches, expected)

        test_text = "This is text"
        expected = []
        matches = extract_markdown_images(test_text)
        #print(f"Test extract_markdown_images({test_text})=={expected}")
        self.assertListEqual(matches, expected)


    def test_extract_markdown_links(self):
        test_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = []
        matches = extract_markdown_links(test_text)
        #print(f"Test extract_markdown_links({test_text})=={expected}")
        self.assertListEqual(matches, expected)

        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        matches = extract_markdown_links(test_text)
        #print(f"Test extract_markdown_links({test_text})=={expected}")
        self.assertListEqual(matches, expected)

        test_text = "This is text"
        expected = []
        matches = extract_markdown_links(test_text)
        #print(f"Test extract_markdown_links({test_text})=={expected}")
        self.assertListEqual(matches, expected)

    def test_extract_title(self):
        test_text = "#hello"
        expected = "hello"
        res = extract_title(test_text)
        #print(f"Test extract_title({test_text})=={expected}")
        self.assertEqual(res, expected)

        test_text = "blabla\n#hello"
        expected = "hello"
        res = extract_title(test_text)
        #print(f"Test extract_title({test_text})=={expected}")
        self.assertEqual(res, expected)

        test_text = "##blabla\n#hello"
        expected = "hello"
        res = extract_title(test_text)
        #print(f"Test extract_title({test_text})=={expected}")
        self.assertEqual(res, expected)

        test_text = "#hello\nblabla"
        expected = "hello"
        res = extract_title(test_text)
        #print(f"Test extract_title({test_text})=={expected}")
        self.assertEqual(res, expected)

        test_text = "##hello"
        expected = "No title in provided markdown"
        #print(f"Test extract_title({test_text})=={expected}")
        with self.assertRaises(Exception, msg=expected) as cm:
            res = extract_title(test_text)
        self.assertEqual(str(cm.exception), expected)

        test_text = ""
        expected = "No title in provided markdown"
        #print(f"Test extract_title({test_text})=={expected}")
        with self.assertRaises(Exception, msg=expected) as cm:
            res = extract_title(test_text)
        self.assertEqual(str(cm.exception), expected)

        test_text = "bimbombimbom\nbonjour"
        expected = "No title in provided markdown"
        #print(f"Test extract_title({test_text})=={expected}")
        with self.assertRaises(Exception, msg=expected) as cm:
            res = extract_title(test_text)
        self.assertEqual(str(cm.exception), expected)



if __name__ == "__main__":
    unittest.main()
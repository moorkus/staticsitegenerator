from enum import Enum
import re
from htmlnode import *
from textnode import *
from split_nodes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(text: str) -> list[str]:
    text = text.strip()
    res = text.split("\n\n")
    for i in range(0, len(res), -1):
        if res[i].isspace():
            res.pop(i)
    return res

def block_to_block_type(text: str) -> BlockType:
    if re.fullmatch(r'^\#{1,6} (.|\s)*$', text):
        return BlockType.HEADING
    if re.fullmatch(r'^```\n(.|\s)*```$', text):
        return BlockType.CODE

    splits = text.split("\n")
    quote = True
    un_list = True
    or_list = True
    for i in range(len(splits)):
        if not re.fullmatch(r'^>.*$', splits[i]):
            quote = False
        if not re.fullmatch(r'^- .*$', splits[i]):
            un_list = False
        if not re.fullmatch(r'^' + str(i+1) + r'\. .*$', splits[i]):
            or_list = False
    if quote: return BlockType.QUOTE
    if un_list: return BlockType.UNORDERED_LIST
    if or_list: return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children_blocks = []
    for b in blocks:
        b_type = block_to_block_type(b)
        match b_type:
            case BlockType.CODE:
                children_blocks.append(ParentNode("pre",[LeafNode("code", b.strip("`").lstrip("\n"))]))
            case BlockType.HEADING:
                children_blocks.append(LeafNode("h" + str(len(re.findall(r'^\#*', b)[0])), b.lstrip("# ")))
            case BlockType.ORDERED_LIST:
                children = []
                for l in b.split("\n"):
                    #children.append(LeafNode("li", l.lstrip("0123456789. ")))
                    children_ol = text_to_textnodes(l.lstrip("0123456789. "))
                    children_ol_leaf = []
                    for c in children_ol:
                        children_ol_leaf.append(text_node_to_html_node(c))
                    children.append(ParentNode("li", children_ol_leaf))
                children_blocks.append(ParentNode("ol", children))
            case BlockType.PARAGRAPH:
                children = []
                text_nodes = text_to_textnodes(b)
                for t in text_nodes:
                    children.append(text_node_to_html_node(t))
                children_blocks.append(ParentNode("p", children))
            case BlockType.QUOTE:
                children_blocks.append(LeafNode("blockquote", b.replace(">", "").lstrip()))
            case BlockType.UNORDERED_LIST:
                children = []
                for l in b.split("\n"):
                    #children.append(LeafNode("li", l.lstrip("- ")))
                    children_ul = text_to_textnodes(l.lstrip("- "))
                    children_ul_leaf = []
                    for c in children_ul:
                        children_ul_leaf.append(text_node_to_html_node(c))
                    children.append(ParentNode("li", children_ul_leaf))
                children_blocks.append(ParentNode("ul", children))
            case _:
                raise Exception(f"Block type {b_type} not recognized for block :{b}")
        
    return ParentNode("div", children_blocks)

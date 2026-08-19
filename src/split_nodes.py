from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    res = []
    for o in old_nodes:
        # if delimiter not in o.text:
        #         raise Exception(f"Specified delimitor not in \"{o.text}\"")
        if o.text_type != TextType.TEXT:
            res.append(o)
        else:
            split_txt = o.text.split(delimiter)
            if len(split_txt) %2 == 0:
                raise Exception(f"\"{o.text}\" has an uneven amount of \'{delimiter}\'")
            for i in range (len(split_txt)):
                if i%2 == 0:
                    res.append(TextNode(split_txt[i], TextType.TEXT))
                else:
                    match delimiter:
                        case "`":
                            res.append(TextNode(split_txt[i], TextType.CODE))
                        case "**":
                            res.append(TextNode(split_txt[i], TextType.BOLD))
                        case "_":
                            res.append(TextNode(split_txt[i], TextType.ITALIC))
                        case _:
                            raise Exception(f"Unrecognized delimiter \'{delimiter}\'")
    return res

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for n in old_nodes:
        extr = extract_markdown_images(n.text)
        l = len(extr)
        if l == 0:
            res.append(n)
            continue
        sections = [n.text]
        for i in range(l):
            sections = sections[0].split(f"![{extr[i][0]}]({extr[i][1]})", 1)
            res.append(TextNode(sections[0], TextType.TEXT))
            res.append(TextNode(extr[i][0], TextType.IMAGE, extr[i][1]))
            sections.pop(0)
        if len(sections) and sections[0] != "": res.append(TextNode(sections[0], TextType.TEXT))
    return res
    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for n in old_nodes:
        extr = extract_markdown_links(n.text)
        l = len(extr)
        if l == 0:
            res.append(n)
            continue
        sections = [n.text]
        for i in range(l):
            sections = sections[0].split(f"[{extr[i][0]}]({extr[i][1]})", 1)
            res.append(TextNode(sections[0], TextType.TEXT))
            res.append(TextNode(extr[i][0], TextType.LINK, extr[i][1]))
            sections.pop(0)
        if len(sections) and sections[0] != "": res.append(TextNode(sections[0], TextType.TEXT))
    return res

def text_to_textnodes(text: str) -> list[TextNode]:
    res = [TextNode(text, TextType.TEXT)]
    res = split_nodes_delimiter(res, "**", TextType.TEXT)
    res = split_nodes_delimiter(res, "`", TextType.TEXT)
    res = split_nodes_delimiter(res, "_", TextType.TEXT)
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    return res


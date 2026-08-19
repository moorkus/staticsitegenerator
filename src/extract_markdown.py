import re

def extract_markdown_images(text: str) -> list[tuple]:
    return  re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    
def extract_markdown_links(text: str) -> list[tuple]:
    return  re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def extract_title(markdown: str) -> str:
    res = []
    res = re.findall(r"(?:^|\n)#([^#]*?)(?:$|\n)", markdown)
    if len(res) == 0:
        raise Exception("No title in provided markdown")
    return res[0]
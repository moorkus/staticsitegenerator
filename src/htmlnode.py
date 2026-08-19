import re

class HTMLNode():
    def __init__(self, \
                tag: str = None, \
                value: str = None, \
                children: list["HTMLNode"] = None, \
                props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        res = ""
        if self.props == None:
            return res
        for e in self.props:
            res += " "
            res += e
            res += "="
            res += '"' + self.props[e] + '"'
        return res

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {str(self.children)}, {self.props_to_html()})"


class LeafNode(HTMLNode):
    def __init__(self, \
            tag: str, \
            value: str, \
            props: dict = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("value missing")
        if self.tag == None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"

class ParentNode(HTMLNode):
    def __init__(self, \
            tag: str, \
            children: list["HTMLNode"], \
            props: dict = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("tag missing")
        if self.children == None:
            raise ValueError("children missing")
        res = f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            res += c.to_html()
        res += f"</{self.tag}>"
        return res

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {str(self.children)}, {self.props_to_html()})"

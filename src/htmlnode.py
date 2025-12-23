class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == "" or self.props == {}:
            return ""
        return f' href="{self.props["href"]}" target="{self.props["target"]}"'
    
    def __eq__(self, other):
        if self.tag != other.tag:
            return False
        elif self.value != other.value:
            return False
        elif self.children != other.children:
            return False
        elif self.props != other.props:
            return False
        else:
            return True

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        else:
            parent_html = ""
            for child in self.children:
                parent_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{parent_html}</{self.tag}>"
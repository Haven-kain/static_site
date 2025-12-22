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
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("LeafNodes must have a value")
        elif self.tag == None or self.tag == "":
            return self.value
        else:
            prop_string = self.props_to_html()
            return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"
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
        
        attrs = ""
        for key in self.props:
            value = self.props[key]
            attrs += f' {key}="{value}"'
        return attrs
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None or self.tag == "":
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent nodes must have a tag")
        if self.children == None or self.children == []:
            raise ValueError("PArent nodes must have children")
        
        parent_html = ""
        for child in self.children:
            parent_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{parent_html}</{self.tag}>"
    
    # Create a document and add the root node.
    wx.XmlDocument xmlDoc
    
    wx.XmlNode* root = wx.XmlNode(NULL, wx.XML_ELEMENT_NODE, "Root")
    xmlDoc.SetRoot(root)
    
    # Add some XML.
    wx.XmlNode* library = wx.XmlNode (root, wx.XML_ELEMENT_NODE, "Library")
    library.AddAttribute("type", "CrossPlatformList")
    wx.XmlNode* name = wx.XmlNode(library, wx.XML_ELEMENT_NODE, "Name")
    name.AddChild(wx.XmlNode(wx.XML_TEXT_NODE, "", "wx.Widgets"))
    
    # Write the output to a wx.String.
    wx.StringOutputStream stream
    xmlDoc.Save(stream)

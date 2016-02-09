    
    wx.Image image
    image.SetLoadFlags(image.GetLoadFlags() & ~wx.Image.Load_Verbose)
    image.LoadFile(...)

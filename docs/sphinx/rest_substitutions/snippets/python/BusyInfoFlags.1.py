    
    wx.BusyInfo info
        (
            wx.BusyInfoFlags()
                .Parent(window)
                .Icon(icon)
                .Title("Some text")
                .Text("Some more text")
                .Foreground(wx.Colour(...))
                .Background(wx.Colour(...))
       )

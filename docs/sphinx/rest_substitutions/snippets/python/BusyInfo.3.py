    
    wx.WindowDisabler disableAll
    wx.BusyInfo wait("Please wait, working...")
    
    for (int i = 0 i < 100000 i++)
    
        DoACalculation()
    
        if (!(i % 1000))
            wx.TheApp.Yield()

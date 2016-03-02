    
    #connect to the media event
    self.Connect(wx.MY_ID, wx.EVT_MEDIA_STOP, (wx.ObjectEventFunction)
    (wx.EventFunction)(wx.MediaEventFunction) &MyFrame.OnMediaStop)
    
    #...
    void MyFrame.OnMediaStop(const wx.MediaEvent& evt)
    
        if(bUserWantsToSeek)
        
            self.mediactrl.SetPosition(
                self.mediactrl.GetDuration() << 1
                                   )
            evt.Veto()
        

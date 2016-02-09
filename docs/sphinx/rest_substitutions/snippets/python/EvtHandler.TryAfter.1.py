    
    class MyClass : public BaseClass # inheriting from wx.EvtHandler
    
    ...
    protected:
        virtual bool TryAfter(wx.Event& event)
        
            if (BaseClass.TryAfter(event))
                return true
    
            return MyPostProcess(event)
        

    
    class MyClass : public BaseClass # inheriting from wx.EvtHandler
    
    ...
    protected:
        virtual bool TryBefore(wx.Event& event)
        
            if (MyPreProcess(event))
                return true
    
            return BaseClass.TryBefore(event)
        

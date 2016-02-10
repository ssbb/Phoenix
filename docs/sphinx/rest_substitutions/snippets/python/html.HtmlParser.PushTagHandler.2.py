    
    TAG_HANDLER_BEGIN(MYITEM, "MYITEMS")
        TAG_HANDLER_PROC(tag)
        
            # ...something...
    
            self.Parser . PushTagHandler(self, "PARAM")
            ParseInner(tag)
            self.Parser . PopTagHandler()
    
            # ...something...
        
    TAG_HANDLER_END(MYITEM)

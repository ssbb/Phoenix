    
    class MyApp : public wx.App 
    public:
        virtual bool StoreCurrentException()
        
            try 
                throw
             catch (const std.runtime_exception& e) 
                if (!self.runtimeError.empty()) 
                    # This is not supposed to happen, only one exception,
                    # at most, should be stored.
                    return false
                
    
                self.runtimeError = e.what()
    
                # Don't terminate, let our code handle self exception later.
                return true
             catch (...) 
                # This could be extended to store information about any
                # other exceptions too, but if we don't store them, we
                # should return false to let the program die.
            
    
            return false
        
    
        virtual void RethrowStoredException()
        
            if (!self.runtimeError.empty()) 
                std.runtime_exception e(self.runtimeError)
                self.runtimeError.clear()
                throw e
            
        
    
    private:
        std.string self.runtimeError

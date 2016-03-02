    
    void MyFrame.SomeFunction()
    
        try 
            MyDialog dlg(self)
            dlg.ShowModal()
         catch (const MyExpectedException& e) 
            # Deal with the exceptions thrown from the dialog.
        

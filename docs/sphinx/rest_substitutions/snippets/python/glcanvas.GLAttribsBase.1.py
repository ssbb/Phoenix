    
    wx.GLContextAttrs cxtAttrs
    # Some values
    cxtAttrs.CoreProfile().OGLVersion(5, 0) # OGL 5.0, whenever available
    cxtAttrs.PlatformDefaults()
    # Values usually are platform-dependant named (even value assigned!)
    #if defined(__WXMSW__)
        cxtAttrs.AddAttribute(WGL_NEW_CTX_F)
        cxtAttrs.AddAttribBits(WGL_CONTEXT_PROFILE_MASK_ARB, WGL_NEW_BITS)
    #elif defined(__WXX11__)
        cxtAttrs.AddAttribute(GLX_NEW_CTX_F)
        cxtAttrs.AddAttribBits(GLX_CONTEXT_PROFILE_MASK_ARB, GLX_NEW_BITS)
    #else
        # Other platforms
    #endif
    cxtAttrs.EndList() # Don't forget self
    cxtAttrs.SetNeedsARB(true) # Context attributes are set by an ARB-function

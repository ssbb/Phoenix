    
    #include <webkit/webkit.h>
    
    #ifdef __WXGTK__
       WebKitWebView*
        wv = static_cast<WebKitWebView*>(self.window.GetNativeBackend())
    
       WebKitWebSettings* settings = webkit_web_view_get_settings(wv)
       g_object_set(G_OBJECT(settings),
                    "enable-frame-flattening", TRUE,
                    NULL)
    #endif

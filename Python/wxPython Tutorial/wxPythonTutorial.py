import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)


        # self.Move((250,250)) # to change the location where the window appears


        self.Center() # to make the window appear in the center of the screen
        
        self.Show() # to make the window pop up


app = wx.App()
windowClass(None, title='epic window!')
app.MainLoop()


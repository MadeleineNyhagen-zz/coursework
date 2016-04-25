import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)

        self.Show()

        


def main():
    app = wx.App()
    window = windowClass(None, title = "Cats!", size =(600,600))
    app.MainLoop()


main()

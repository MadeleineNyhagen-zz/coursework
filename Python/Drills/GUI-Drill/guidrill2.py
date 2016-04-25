#!/usr/bin/env python2

import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)

        # menu
        menuBar = wx.MenuBar()

        # creating menu buttons
        fileButton = wx.Menu()
        editButton = wx.Menu()
        
        # adding menu buttons to menu
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        # to realize menuBar
        self.SetMenuBar(menuBar)

        # to add a Quit button to File menu
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        fileButton.AppendItem(exitItem)

        # bind the Quit button to the Quit function
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        # adding text to panel
        wx.StaticText(panel, label='Pictures of Maru!', pos=(250,30))
        wx.StaticText(panel, label='Isn\'t he cute?', pos=(250,500))

        # adding images to panel
        maru = wx.Image('maru.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.image1 = wx.StaticBitmap(self, -1, maru, (30,60))
        maru2 = wx.Image('maru2.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.image2 = wx.StaticBitmap(self, -1, maru2, (300,60))
        maru3 = wx.Image('maru3.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.image3 = wx.StaticBitmap(self, -1, maru3, (30,270))
        maru4 = wx.Image('maru4.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.image4 = wx.StaticBitmap(self, -1, maru4, (300,270))
        

        self.Show()

    def Quit(self, e):
        self.Close()

        


def main():
    app = wx.App()
    window = windowClass(None, title = "Cats!", size =(600,600))
    app.MainLoop()


main()

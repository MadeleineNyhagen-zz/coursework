# made while following along with the tutorial series here: https://www.youtube.com/playlist?list=PLQVvvaa0QuDc4SQhfpm6XHO0l-1Ybtur2

import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu() # creating a submenu

        importItem.Append(wx.ID_ANY, 'Import Document...') # submenu
        importItem.Append(wx.ID_ANY, 'Import Picture...') # submenu
        importItem.Append(wx.ID_ANY, 'Import Video...') # submenu

        fileButton.AppendMenu(wx.ID_ANY, 'Import', importItem) # submenu

        toolBar = self.CreateToolBar() # creating toolbar
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('maru2.gif')) # toolbar

        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('maru3.gif'))

        toolBar.Realize() # toolbar
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton) # adding quit function to maru picture quit button
        

        # exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit the program')
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('maru.gif'))
        fileButton.AppendItem(exitItem)

        
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)


        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome', 'name')

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()


        yesNoBox = wx.MessageDialog(None, 'Do you enjoy wxPython?', 'Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal() # stores answer to yesNoBox
        yesNoBox.Destroy()


        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'


        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color Question', ['Green','Red','Blue','Yellow'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()


        wx.TextCtrl(panel, pos=(3, 100), size=(150, 50))

        aweText = wx.StaticText(panel, -1, "Awesome Text", (3,3))
        aweText.SetForegroundColour('#67cddc')
        aweText.SetBackgroundColour('black')

        rlyAweText = wx.StaticText(panel, -1, "Customized Awesomeness", (3,30))
        rlyAweText.SetForegroundColour(favColor)
        rlyAweText.SetBackgroundColour('black')
        

        self.SetTitle('Welcome ' + userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None, size =(500,500))

    app.MainLoop()

    
main()

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

        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit the program')
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

        wx.TextCtrl(panel, pos=(10, 10), size=(250, 150))

        if yesNoAnswer == wx.ID_NO:
            userName = 'Loser!'


        chooseOneBox = wx.SingleChoiceDialog(None, 'What is your favorite color?',
                                             'Color Question', ['Green','Red','Blue','Yellow'])
        if chooseOneBox.ShowModal() == wx.ID_OK:
            favColor = chooseOneBox.GetStringSelection()



        

        self.SetTitle('Welcome ' + userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

    
main()

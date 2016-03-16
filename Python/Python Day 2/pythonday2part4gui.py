import wx

class Frame(wx.Frame):
    def __init__(self, title):
        # title = title variable
        wx.Frame.__init__(self, None, title=title, size=(400,600))
        self.Center()

        # add a panel
        panel = wx.Panel(self)

        # add an exit button
        button = wx.Button(panel,label="Exit", size=(100,40),pos=(150,450))
        # bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

        # create menu bar
        menuBar = wx.MenuBar()
        # create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        self.SetMenuBar(menuBar)
        # add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        # add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        # add items to editMenu
        editMenu.Append(wx.NewId(), "Undo")
        editMenu.Append(wx.NewId(), "Redo")
        editMenu.Append(wx.NewId(), "Copy")
        editMenu.Append(wx.NewId(), "Paste")
        # bind exit menu item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

        # add status bar
        self.CreateStatusBar()

        # using the static text widget
        wx.StaticText(panel, label='Characters', pos=(50,30))

        # using the static box widget
        wx.StaticBox(panel, label='Harry Potter Time', pos=(10,10), size=(365,500))

        # using the combo box widget
        harrypotter = ['Cedric', 'Draco', 'Dumbledore', 'Harry', 'Hermione', \
                       'Ginny', 'Luna', 'Mcgonagall', 'Ron', 'Snape']
        cb = wx.ComboBox(panel, pos=(50,50), choices=harrypotter, style=wx.CB_READONLY)

        # using the checkbox widget
        wx.CheckBox(panel, label='Student', pos=(50,80))
        wx.CheckBox(panel, label='Professor', pos=(50,100))

        # using the radio button widget
        wx.RadioButton(panel, label='Gryffindor', pos=(50,130), style=wx.RB_GROUP)
        wx.RadioButton(panel, label='Hufflepuff', pos=(50,150))
        wx.RadioButton(panel, label='Ravenclaw', pos=(50,170))
        wx.RadioButton(panel, label='Slytherin', pos=(50,190))

        # using the text control widget
        wx.TextCtrl(panel, size=(275,-1), pos=(50,220))
        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(275,100), pos=(50,250))

        # using the spin control widget
        # wx.SpinCtrl(panel, value='0', pos=(50,360), size=(70,25))
        sc = wx.SpinCtrl(panel, value='0', pos=(50,360), size=(70,25))
        self.valueText = wx.StaticText(panel, label='', pos=(50,400))
        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)
        

    def exit(self, event):
        self.Destroy()

    def spinControl(self, event):
        # print dir(event)
        # get spin control value
        value = event.GetInt()
        # update static text
        self.valueText.SetLabel(str(value))


app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

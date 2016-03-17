import wx, pythonday2part4gui2database

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
        panel = wx.Panel(self)

        # creating the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        # setup add new character UI
        # create static box
        wx.StaticBox(panel, label='Add a new character', pos=(20,40), size=(280,190))
        # text for name, gender etc
        wx.StaticText(panel, label='Name:', pos=(30,70))
        wx.StaticText(panel, label='Gender:', pos=(30,110))
        wx.StaticText(panel, label='Age:', pos=(30,150))
        wx.StaticText(panel, label='Occupation:', pos=(30,190))
        # single line text boxes
        self.cName = wx.TextCtrl(panel, size=(150,-1), pos=(130,70))
        self.cGen = wx.TextCtrl(panel, size=(150,-1), pos=(130,110))
        self.cAge = wx.SpinCtrl(panel, value='0', pos=(130,150), size=(70,25), min=0, max=2000)
        self.cOcc = wx.TextCtrl(panel, size=(150,-1), pos=(130,190))

        # save button
        save = wx.Button(panel, label="Add Character", pos=(100,230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        # setup the table UI
        # setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        # add columns to listCtrl
        self.listCtrl.InsertColumn(0,'ID')
        self.listCtrl.InsertColumn(1,'Name')
        self.listCtrl.InsertColumn(2,'Gender')
        self.listCtrl.InsertColumn(3,'Age')
        self.listCtrl.InsertColumn(4,'Occupation')

        self.fillListCtrl()

        # setup a delete button
        deleteBtn = wx.Button(panel, label='Delete', pos=(640,450))
        # bind delete button to onDelete function
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

        # run onSelect function when item is selected
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

    def exitProgram(self, event):
        self.Destroy()

    def addCharacter(self, event):
        name = self.cName.GetValue()
        gen = self.cGen.GetValue()
        age = self.cAge.GetValue()
        occ = self.cOcc.GetValue()

        # checking if variables have a value
        if (name =='') or (gen=='') or (age=='') or (occ==''):
            # alert user that a variable is empty
            dlg = wx.MessageDialog(None, 'Some character details are missing. Enter values in each text box.', 'Missing Details', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            return False
        
        # adding character to database
        pythonday2part4gui2database.newCharacter(name, gen, age, occ)
        print pythonday2part4gui2database.viewAll()

        print name
        print gen
        print age
        print occ

        # empty text boxes when finished.
        self.cName.Clear()
        self.cGen.Clear()
        self.cOcc.Clear()
        self.cAge.SetValue(0)

        # update list control
        self.fillListCtrl()

    # get data from the database
    def fillListCtrl(self):
        allData = pythonday2part4gui2database.viewAll()
        # delete old data before adding new data
        self.listCtrl.DeleteAllItems()
        for row in allData:
            # loop through and append data
            self.listCtrl.Append(row)

    # to select an item in the list
    def onSelect(self, event):
        # print event.GetText()
        # get the id of the selected row
        self.selectedID = event.GetText()

    # create a delete function
    def onDelete(self,event):
        # delete the character
        pythonday2part4gui2database.deleteCharacter(self.selectedID)
        # refresh the table
        self.fillListCtrl()



app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

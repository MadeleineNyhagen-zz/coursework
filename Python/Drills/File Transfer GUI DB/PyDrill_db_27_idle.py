import wx, shutil, datetime, os, PyDrill_db
from datetime import datetime, timedelta

class Frame(wx.Frame):
    #added title parameter
    def __init__(self, title):
        #title = title variable
        wx.Frame.__init__(self, None, title='Move Files Created or Modified in Last Twenty-Four Hours', size=(600,400))
        self.Center()
        panel = wx.Panel(self)

        #create menu bar
        menuBar = wx.MenuBar()

        #create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        self.SetMenuBar(menuBar)

        #Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        wx.StaticText(panel, label='Select a source directory:', pos=(30,30))
        self.findFile = wx.DirPickerCtrl(panel, path='C:/Users/stud/Desktop/A',message='Choose a file to move', pos=(50,60))
        self.source = (self.findFile.GetPath())

        checkButton = wx.Button(panel, label="Check For Modified Files", size=(200,30), pos=(50,100))
        checkButton.Bind(wx.EVT_BUTTON, self.getModifiedFiles)

        wx.StaticText(panel, label='Select a destination directory:', pos=(30,170))
        self.moveFileTo = wx.DirPickerCtrl(panel, path='C:/Users/stud/Desktop/B', message='Choose a folder to which to move files:', pos=(50,200))
        self.destination = (self.moveFileTo.GetPath())

        moveButton = wx.Button(panel, label="Move Selected Files", size=(200,30), pos=(50,240))
        moveButton.Bind(wx.EVT_BUTTON, self.moveModifiedFiles)

        self.lastmovedate = wx.TextCtrl(panel, value=PyDrill_db.lastChecked(), size=(300,30), pos=(30,300), style=wx.TE_READONLY)

        cancelButton = wx.Button(panel,label="Cancel",size=(100,30),pos=(380,290))
        #bind button to the function self.exit
        cancelButton.Bind(wx.EVT_BUTTON, self.exit)

        wx.StaticText(panel, label='New and modified files in selected directory:', pos=(300,30))
        self.listOfFiles = wx.ListCtrl(panel, size=(250,220), pos=(300,50), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.listOfFiles.InsertColumn(0,'File Path', width=wx.LIST_AUTOSIZE_USEHEADER)

        self.now = datetime.now()

    #call last modification time of file and return a readable timestamp:

    def modDate(self, filename):
        t = os.path.getmtime(filename)
        return datetime.fromtimestamp(t)

    #call creation time of file and return a readable timestamp:

    def createDate(self, filename):
        t = os.path.getctime(filename)
        return datetime.fromtimestamp(t)

    #to compare the file timestamps to the current time and determine whether they've been modified in the last 24 hours:

    def compDates(self, filenames):
        recentMod = self.now - self.modDate(filenames)
        recentCreate = self.now - self.createDate(filenames)
        if recentMod < timedelta(hours=24) or recentCreate < timedelta(hours=24):
            return True
        else:
            return False
        
    # to list recently created or modified files:

    def getModifiedFiles(self, event):
        for files in os.listdir(self.source):
            path = self.source + "/" + files
            if self.compDates(path):
                self.listOfFiles.Append((path,))

    # to move listed files:

    def moveModifiedFiles(self, event):
        move = False
        for item in range(self.listOfFiles.GetItemCount()):
            path =(self.listOfFiles.GetItem(item).GetText())
            shutil.move(path, self.destination)
            move = True
        if move:
            # creates a message dialog telling user that files were transferred successfully
            dlg = wx.MessageDialog(None, 'Selected files have been successfully transferred.', 'File Transfer Complete', wx.OK)
            PyDrill_db.addTimeStamp()
            self.lastmovedate.SetValue(PyDrill_db.lastChecked())
            self.listOfFiles.DeleteAllItems()
        else:
            # creates message dialog telling user no files were selected to transfer
            dlg = wx.MessageDialog(None, 'Please select files to transfer.', 'No Files Selected', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    # to close GUI:

    def exit(self, event):
        self.Destroy()

app = wx.App()
#pass in the frame title
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

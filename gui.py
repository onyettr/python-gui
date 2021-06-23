#!/usr/bin/env python3.7
#
# Example GUI interface using TKinter
# @author ronyett

# relies on these imports
import sys
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox

# Initial screen dimensions
SCREEN_X = 450
SCREEN_Y = 350

# Version
VERSION_STRING = "V0.1.0-Experimental"            # No name, no slogan

# add gprobe [Option] button
CommandOptionsList = [
        "<Command 1>",
        "<Command 2>",
        "<Command 3>"
    ]
        
class UI:
    def __init__(self, master):
        # Start the main layout
        master.title("UI")
        master.geometry("800x600")
        master.grid_columnconfigure(3)
        master.grid_rowconfigure(100)
        master.grid(sticky=E+W+N+S)          # stretch enabled

        self.master = master
        
        self.WindowInit()                    # Windows frame setup
        self.WindowMenuInit()                # Menus and submenus

    # Create top bar menus and sub-menu items
    #  File
    #  Edit
    #  View
    #  Tools
    #  Macro
    #  Window
    #  Help
    #  Exit
    def WindowMenuInit(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # FILE Menu
        MenuFile = Menu(menu)
        menu.add_cascade(label="File", menu=MenuFile)

        # FILE Submenu -> NEW
        MenuNew = Menu(menu)
        MenuFile.add_command(label="New", command=self.ActionMenuFileNew)        

        # FILE Submenu -> OPEN
        MenuOpen = Menu(menu)
        MenuFile.add_command(label="Open", command=self.ActionMenuFileOpen)        

        # FILE Submenu -> CLOSE
        MenuClose = Menu(menu)
        MenuFile.add_command(label="Close", command=self.ActionMenuFileClose)        

        MenuFile.add_separator()
        
        # FILE Submenu -> SAVE
        MenuSave = Menu(menu)
        MenuFile.add_command(label="Save", command=self.ActionMenuFileSave)        

        # FILE Submenu -> SAVE AS
        MenuSaveAs = Menu(menu)
        MenuFile.add_command(label="Save As", command=self.ActionMenuFileSaveAs)        

        # FILE Submenu -> SAVE ALL
        MenuSaveAll = Menu(menu)
        MenuFile.add_command(label="Save All", command=self.ActionMenuFileSaveAll)        

        MenuFile.add_separator()
        
        # FILE submenu -> Connection Settings
        MenuConnection = Menu(menu)
        MenuFile.add_command(label="Connection Settings", \
                             command=self.ActionMenuConnectionSettings)

        MenuFile.add_separator()
        
        # FILE Submenu Exit
        MenuExit = Menu(menu)
        MenuFile.add_command(label="Exit", command=self.ActionMenuExit)

        # Edit Menu
        MenuEdit = Menu(menu)
#        MenuFile.add_command(label="Edit", command=self.ActionMenuEdit)        
        menu.add_cascade(label="Edit", menu=MenuEdit)

        # View
        MenuView = Menu(menu)
#        MenuFile.add_command(label="View", command=self.ActionMenuView)
        menu.add_cascade(label="View", menu=MenuView)

        # Tools
        MenuTools = Menu(menu)
#        MenuFile.add_command(label="Tools",command=self.ActionMenuTools)
        menu.add_cascade(label="Tools", menu=MenuTools)

        # Macro
        MenuMacro = Menu(menu)
#        MenuFile.add_command(label="Macro", command=self.ActionMenuMacro)
        menu.add_cascade(label="Macros", menu=MenuMacro)

        # Window
        MenuWindow = Menu(menu)
#        MenuFile.add_command(label="Window", command=self.ActionMenuWindow)
        menu.add_cascade(label="Window", menu=MenuWindow)

        # Help & Sub menus
        MenuHelp = Menu(menu)
        menu.add_cascade(label="Help", menu=MenuHelp, command=self.ActionMenuHelp)

        MenuAbout= Menu(menu)
        MenuHelp.add_command(label="About", command=self.ActionHelpAbout)

    #
    # Main frame (GUI) construction
    #
    def WindowInit(self):
        # add gprobe command line text entry box
        self.CmdLine = Entry(self.master,width=70)
        self.CmdLine.grid(column=0, row=0)
        self.CmdLine.bind('<Return>',self.ActionGoEntry)           # [ENTER] will execute the command line
        self.CmdLine.bind('<Up>'    ,self.ActionCmdHistoryScroll)  # <up>    will scroll up history
        self.CmdLine.bind('<Down>'  ,self.ActionCmdHistoryScroll)  # <down>  will scroll down history        
        self.CmdLine.CmdHistory = []                               # History of Command lines
        self.CmdLine.CmdLastIndex = None
        
        # add gprobe [GO] button to execute
        self.GoButton = Button(self.master, text="[GO]", command=self.ActionGo)
        self.GoButton.grid(column=1, row=0)
        
        self.OptionButton = Menubutton(self.master,text="Options")
        self.OptionButton.grid(column=3, row=0)
        self.OptionButton.menu = Menu(self.OptionButton)
        self.OptionButton["menu"] = self.OptionButton.menu
        self.WhichOption = StringVar()
        for i in range(len(CommandOptionsList)):
            self.OptionButton.menu.add_radiobutton(label=CommandOptionsList[i],
                                                   command  = self.CommandOptionCallBack,
                                                   variable = self.WhichOption)

        # add [CLOSE] button
        self.CloseButton = Button(self.master, text="Close", \
                                  command=self.master.quit)
        self.CloseButton.grid(column=1, row=5)

        # progress bar, should be at the bottom of the screen
        self.Style = ttk.Style()
        self.Style.theme_use ('default')
        self.Style.configure("black.Horizontal.TProgressbar", background='blue')
        # self.ProgBar = Progressbar(self.master, length=600, style='black.Horizontal.TProgressbar')
        # self.ProgBar['value'] = 50
        # self.ProgBar.grid(column=0,row=50)

        # Console area
        self.Console = scrolledtext.ScrolledText(self.master)
        self.Console.grid(row=3,column=0)

        self.CmdLine.focus()       # Start with this entry

    def AddWindowText(self,text):
        self.Console.insert(INSERT,text)

    #
    # MENU Operations
    #
    def ActionMenuExit(self):
        self.AddWindowText("[MENU] Exit\n")
        self.master.quit        

    def ActionMenuEdit(self):
        self.AddWindowText("[MENU] Edit\n")

    def ActionMenuFileNew(self):
        self.AddWindowText("[MENU] File New\n")
        
    def ActionMenuFileOpen(self):
        self.AddWindowText("[MENU] File Open\n")

    def ActionMenuFileClose(self):
        self.AddWindowText("[MENU] File Close\n")
        
    def ActionMenuFileSave(self):
        self.AddWindowText("[MENU] File Save\n")
        
    def ActionMenuFileSaveAs(self):
        self.AddWindowText("[MENU] File Save As\n")

    def ActionMenuFileSaveAll(self):
        self.AddWindowText("[MENU] File Save All\n")
        
    def ActionMenuConnectionSettings(self):
        self.AddWindowText("[MENU] Connection Settings\n")
        messagebox.showinfo("Connection", "TODO")        

    def ActionMenuWindow(self):
        self.AddWindowText("[MENU] Window\n")

    def ActionMenuView(self):
        self.AddWindowText("[MENU] View\n")
        
    def ActionMenuTools(self):
        self.AddWindowText("[MENU] Tools\n")

    def ActionMenuMacro(self):
        self.AddWindowText("[MENU] Macro\n")
        
    def ActionHelpAbout(self):
        self.AddWindowText("[MENU] About\n")
        messagebox.showinfo("Gprobe", "Gprobe V1.0.0")

    def ActionMenuHelp(self):
        self.AddWindowText("[MENU] Help\n")

    def HelpCallBack():
        showinfo('About', VERSION_STRING)

    #
    # Commandline actions
    #
    def CommandOptionCallBack(self):
        print("Option " + self.WhichOption.get())
        cmd = self.WhichOption.get()
        cmd = cmd.split(" ")
        self.CmdLine.insert(0,cmd[0])

    def CommandLineValidate(self, newString):
        print("CommandLineValidate: ")

    def GetCommandLine(self):
        return self.CmdLine.get()
    
    def EntryGetCommandLine(self):
        CmdLine = self.GetCommandLine()               # obtain the commandline from the Entry box
        self.AddWindowText("[GO]->> " + CmdLine + '\n')
        self.CmdLine.delete(0,'end')            # Clear previous command line entry 

        # add to history
        if CmdLine not in self.CmdLine.CmdHistory:  # Test if we have this already
            self.CmdLine.CmdHistory.append(CmdLine) # add to command line history
            self.CmdLine.CmdLastIndex = len(self.CmdLine.CmdHistory)-1
            print("History->",  self.CmdLine.CmdHistory)        

    # 
    def ActionCmdHistoryScroll(self, event):
        print("[ActionCmdHistoryScroll] ", event)
        
        if not self.CmdLine.CmdLastIndex is None:
            self.CmdLine.delete(0,'end')        # Clear previous entry            

            if event.keysym == 'Up':                  # Scroll up
                if self.CmdLine.CmdLastIndex > 0:
                    self.CmdLine.CmdLastIndex -= 1
                else:
                    self.CmdLine.CmdLastIndex  = len(self.CmdLine.CmdHistory) - 1
                    print(self.CmdLine.CmdLastIndex)
                    
            elif event.keysym == 'Down':
                if self.CmdLine.CmdLastIndex < len(self.CmdLine.CmdHistory) - 1:
                    self.CmdLine.CmdLastIndex += 1
                else:
                    self.CmdLine.CmdLastIndex = 0
            # add scrolled item to Entry box command line                    
            self.CmdLine.insert(0, self.CmdLine.CmdHistory[self.CmdLine.CmdLastIndex])
        
    def ActionGoEntry(self,event):
        self.EntryGetCommandLine()

    def ActionGo(self):
        self.EntryGetCommandLine()
        
# create main "screen"
if __name__ == '__main__' :
    try:    
        Windowroot = Tk()
        print("[INFO] UI Main window created")
    except:
        print(f"\033[31m[ERROR] oops - Requires X win environment\033[0m", sys.exc_info()[0])
        sys.exit()

    myGui = UI(Windowroot)
    myGui.AddWindowText("UI experimental\n")

    Windowroot.mainloop()    # run until done...
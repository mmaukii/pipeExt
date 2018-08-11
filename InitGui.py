class MyWorkbench (Workbench):

    MenuText = "My Workbench"
    ToolTip = "A description of my workbench"
    Icon = """
 			/* XPM */
 			static const char *test_icon[]={
 			"16 16 2 1",
 			"a c #000000",
 			". c None",
 			"................",
 			"................",
 			"..############..",
 			"..############..",
 			"..############..",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"......####......",
 			"................",
 			"................"};
 			"""

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import pipeExtModul # import here all the needed files that create your FreeCAD commands
        self.list = ["pipeMenu","pipeParts"] # A list of command names created in the line above
        self.appendToolbar("My Commands",self.list) # creates a new toolbar with your commands
        #self.appendMenu("My New Menu",self.list) # creates a new menu
        #self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands",self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
       
Gui.addWorkbench(MyWorkbench())
#https://www.freecadweb.org/wiki/Command
import FreeCAD,FreeCADGui
class MyCommand:
	def __init__(self):# you can add things here like defining some variables that must exist at all times
		print ("init")
		
	def GetResources(self):
		return {'Accel' : "Ctrl+A",
				'MenuText': QtCore.QT_TRANSLATE_NOOP("My_Command", "My Command"),
				'ToolTip': QtCore.QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

	def Activated(self):
		print("hui")
		# place here the code to be executed when the command is ran

	def isActive(self):
		print("Active commmand")
		# here you have a chance to return True or False depending if your command must be shown as active or inactive (greyed).

# the command must be "registered" in FreeCAD's command system
FreeCADGui.addCommand('My_Command',MyCommand()) 
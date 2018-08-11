# -*- coding: utf-8 -*-
import FreeCAD,FreeCADGui
class pipeMenu:
	"Menu to change pipes"
	def GetResources(self):
		return {"MenuText": "My Command",
				"Accel": "Ctrl+M",
				"ToolTip": "Menu for pipe properties",
				"Pixmap": FreeCAD.__path__[0].encode('ascii','ignore') + "\pipeExt\icons\pipeMenu.svg"}

	def IsActive(self):
		return True #if true not grayed out

	def Activated(self):
		import pipeMenu
		pipeMenu
				
class pipeParts:
	"Change Valves and stuff in pipes"
	def GetResources(self):
		return {"MenuText": "My Command",
				"Accel": "Ctrl+P",
				"ToolTip": "Insert something in your pipe",
				"Pixmap": FreeCAD.__path__[0].encode('ascii','ignore') + "\pipeExt\icons\pipeParts.svg"}

	def IsActive(self):
		return True #if true not grayed out

	def Activated(self):
		import pipeParts 
		a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Armatur")
		pipeParts.Valve(a)
		pipeParts.ViewProviderValve(a.ViewObject)
		FreeCAD.ActiveDocument.recompute()

				
				
class pipeReduction:
	"Adds a Reduction to the pipe"
	def GetResources(self):
		return {"MenuText": "My Command",
				"Accel": "Ctrl+R",
				"ToolTip": "Adds a Reduction to the end of the pipe",
				"Pixmap": FreeCAD.__path__[0].encode('ascii','ignore') + "\pipeExt\icons\pipeReduction.svg"}

	def IsActive(self):
		return True #if true not grayed out

	def Activated(self):
		import pipeReduction
		a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Reduction")
		pipeReduction.Reduction(a)
		pipeReduction.ViewProviderReduction(a.ViewObject)
		FreeCAD.ActiveDocument.recompute() 
				
				
				
FreeCADGui.addCommand('pipeMenu',pipeMenu())
FreeCADGui.addCommand('pipeParts',pipeParts())
FreeCADGui.addCommand('pipeReduction',pipeReduction())
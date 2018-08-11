# -*- coding: utf-8 -*-
import FreeCAD,FreeCADGui
class MyTool:
	"My tool object"
	def GetResources(self):
		return {"MenuText": "My Command",
				"Accel": "Ctrl+M",
				"ToolTip": "My extraordinary command",
				"Pixmap": FreeCAD.__path__[0].encode('ascii','ignore') + "\pipeExt\icons\pipeMenu.svg"}

	def IsActive(self):
		return True #if true not grayed out

	def Activated(self):
		#Im Ordner in dem das 3d Modell liegt müssen auch folgende Dateien liegen:
		#Rohrdefinitionen.csv ,DN_Durchmesser.csv
		#macro loops through selection
		#if one pipe selected in reads into the fields on startup
		#if multiple pipes are in the selection, all fields are empty, only values which 

		#Quelle: https://www.freecadweb.org/wiki/PySide_Medium_Examples
		# import statements
		#execfile(App.getUserAppDataDir()+"Macro\\Rohrfuhrung_benennen1.FCMacro")
		from PySide import QtGui, QtCore
		import numpy as np
		sel = FreeCADGui.Selection.getSelection()
		guiDoc = FreeCADGui.ActiveDocument
		# UI Class definitions
		DNarray = np.genfromtxt(FreeCAD.__path__[0].encode('ascii','ignore') +  '\pipeExt\Resources\DN_Durchmesser.csv', delimiter=',', names=True)
		RohrDef = np.genfromtxt(FreeCAD.__path__[0].encode('ascii','ignore') +  '\pipeExt\Resources\Rohrdefinitionen.csv', delimiter=',', names=True,dtype=None)
		#print(RohrDef.dtype.names)
		#print(RohrDef)
		# List all objects of the document
		doc = FreeCAD.ActiveDocument

		sel = FreeCADGui.Selection.getSelection()
		#loop through selection to search for pipes
		iPipe=0
		indexPipe = []
		for o in sel:
			#print o.Name
			if "Pipe" in o.Name :
				iPipe=iPipe+1
				indexPipe.append(iPipe)


		#if  not FreeCADGui.Selection.getSelection() :

		class ExampleModalGuiClass(QtGui.QDialog):
			""""""

			GaebExport = True
			def __init__(self):
				super(ExampleModalGuiClass, self).__init__()
				self.initUI()
			def initUI(self):
				#here again (like above) for the update function
				sel = FreeCADGui.Selection.getSelection()
				#loop through selection to search for pipes
				iPipe=0
				indexPipe = []
				for o in sel:
					#print o.Name
					if "Pipe" in o.Name :
						iPipe=iPipe+1
						indexPipe.append(iPipe)
						
				self.result = userCancelled
				# create our window
				# define window		xLoc,yLoc,xDim,yDim
				self.setGeometry(	250, 250, 400, 220)
				self.setWindowTitle("Rohrmanipulation H2Office")
				self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
				
				# Rohrbezeichnung
				self.label2 = QtGui.QLabel("Rohrbezeichung:", self)
				self.label2.move(20, 20)
				self.textInputBez = QtGui.QLineEdit(self)
				self.textInputBez.setFixedWidth(150)
				self.textInputBez.move(20, 35)
				
				# Medium
				self.label2 = QtGui.QLabel("Medium:", self)
				self.label2.move(220, 20)
				self.popupItems1 = [""]+RohrDef["Medium"].tolist()
				self.popupMedium = QtGui.QComboBox(self)
				self.popupMedium.addItems(self.popupItems1)
				#self.popupMedium.setCurrentIndex(self.popupItems1.index("Faulgas"))
				self.popupMedium.activated[str].connect(self.onpopupMedium)
				self.popupMedium.move(220, 35)
				
				# # DN
				self.label2 = QtGui.QLabel("DN:", self)
				self.label2.move(330, 20)
				self.popupItems2 = [""]+[ '{:.0f}'.format(x) for x in DNarray["DN"]]
				self.popupDN = QtGui.QComboBox(self)
				self.popupDN.addItems(self.popupItems2)
				self.popupDN.move(330, 35)
				
				# # Material
				self.label3 = QtGui.QLabel("Material:", self)
				self.label3.move(20, 60)
				self.popupItems3 = [""]+np.unique(RohrDef["Material"]).tolist()
				self.popupMaterial = QtGui.QComboBox(self)
				self.popupMaterial.addItems(self.popupItems3)
				self.popupMaterial.move(20, 75)
				
				# Gaeb Ja nein
				self.checkboxGaeb = QtGui.QCheckBox("Gaebexport Rohrleitung", self)
				self.checkboxGaeb.clicked.connect(self.oncheckboxGaeb)
				self.checkboxGaeb.setTristate()
				self.checkboxGaeb.setCheckState(QtCore.Qt.PartiallyChecked)
				self.checkboxGaeb.move(20,100)		
						
				# Gaeb Bereich
				self.label11 = QtGui.QLabel("Gaeb Bereich:", self)
				self.label11.move(20, 120)
				self.textInputGaebBereich = QtGui.QLineEdit(self)
				self.textInputGaebBereich.setFixedWidth(150)
				self.textInputGaebBereich.move(20, 140)
					
				# Gaeb Gruppe
				self.label11 = QtGui.QLabel("Gaeb Gruppe:", self)
				self.label11.move(220, 120)
				self.textInputGaebGruppe = QtGui.QLineEdit(self)
				self.textInputGaebGruppe.setFixedWidth(150)
				self.textInputGaebGruppe.move(220, 140)
				

				# cancel button
				clearButton = QtGui.QPushButton('Clear input', self)
				clearButton.clicked.connect(self.onClear)
				clearButton.move(140,170)
				
				# OK button
				setButton = QtGui.QPushButton('Set Properties', self)
				setButton.clicked.connect(self.onSet)
				setButton.setAutoDefault(True)
				setButton.move(20, 170) 
				
				# Pipe show Button
				self.pipeShowButton = QtGui.QPushButton("Rohre ausblenden", self)
				self.pipeShowButton.setCheckable(True)
				self.pipeShowButton.clicked.connect(self.onpipeShow)
				self.pipeShowButton.move(20, 195) 

				# Pipe lines show Button
				self.pipeShowLineButton = QtGui.QPushButton("Rohrlinien ausblenden", self)
				self.pipeShowLineButton.setCheckable(True)
				self.pipeShowLineButton.clicked.connect(self.onpipeLineShow)
				self.pipeShowLineButton.move(140, 195) 


				# update button
				updateButton = QtGui.QPushButton('Get Properties', self)
				updateButton.clicked.connect(self.onupdate)
				updateButton.setAutoDefault(True)
				updateButton.move(220, 170)
				
				# update button
				updateButton = QtGui.QPushButton('Set Selection', self)
				updateButton.clicked.connect(self.onsetSel)
				updateButton.setAutoDefault(True)
				updateButton.move(300, 170)

				
				self.show()

				#Füllen der Felder wenn nur ein RohrDef
				if  iPipe==1 :
					#get Name of Pipe, change to string from unicode, get only part without standard naming part
					self.textInputBez.setText(sel[0].Label.encode('ascii','ignore').split("_Rohr",1)[0])
				
				if  iPipe>=1 :	
					if hasattr(sel[0],"Medium"):
						self.popupMedium.setCurrentIndex(self.popupMedium.findText(str(sel[0].Medium)))
					if hasattr(sel[0],"Rohrmaterial"):
						self.popupMaterial.setCurrentIndex(self.popupMaterial.findText(str(sel[0].Rohrmaterial)))
					if hasattr(sel[0],"DN"):
						self.popupDN.setCurrentIndex(self.popupDN.findText(str(sel[0].DN)))#
					if hasattr(sel[0],"GaebBereich"):
						self.textInputGaebBereich.setText(sel[0].GaebBereich)
					if hasattr(sel[0],"GaebGruppe"):
						self.textInputGaebGruppe.setText(sel[0].GaebGruppe)
					if hasattr(sel[0],"GaebExport"):
						self.checkboxGaeb.setChecked(sel[0].GaebExport)
				#loopen durch auswahl, vergleich mit sel 0 wenn ungleich dann feld leeren
				for o in sel[1:]:
					if hasattr(o,"Medium") &  hasattr(sel[0],"Medium"):
						if o.Medium != sel[0].Medium:
							self.popupMedium.setCurrentIndex(-1)
					if hasattr(o,"Rohrmaterial") & hasattr(sel[0],"Rohrmaterial"):
						if o.Rohrmaterial != sel[0].Rohrmaterial:
							self.popupMaterial.setCurrentIndex(-1)
					if hasattr(o,"DN") & hasattr(sel[0],"DN"):
						if o.DN != sel[0].DN:
							self.popupDN.setCurrentIndex(-1)
					if hasattr(o,"GaebBereich") & hasattr(sel[0],"GaebBereich"):
						if o.GaebBereich != sel[0].GaebBereich:
							self.textInputGaebBereich.setText("")
					if hasattr(o,"GaebGruppe") & hasattr(sel[0],"GaebGruppe"):
						if o.GaebGruppe != sel[0].GaebGruppe:
							self.GaebGruppe.setText("")
					if hasattr(o,"GaebExport") & hasattr(sel[0],"GaebExport"):
						if o.GaebExport != sel[0].GaebExport:
							self.GaebExport.setCheckState(QtCore.Qt.PartiallyChecked)
							
				
				if self.popupMedium.currentText()=="" :
					print ("leer")
				
			def onpopupMedium(self, selectedText):
				iii = str(RohrDef["Medium"].tolist().index(self.popupMedium.currentText()))
				self.popupMaterial.setCurrentIndex(self.popupMaterial.findText(str(RohrDef["Material"][iii])))
				

			def oncheckboxGaeb(self):
				print(type(str(self.checkboxGaeb.checkState() )))
				if  self.checkboxGaeb.isChecked():    
					self.GaebExport = True
					print("checkeD")
				else :
					self.GaebExport = False
					print("uncheckeD")

			def onClear(self):
				self.textInputBez.setText("")
				self.popupMedium.setCurrentIndex(-1)		
				self.popupMaterial.setCurrentIndex(-1)		
				self.popupDN.setCurrentIndex(-1)		
				self.textInputGaebBereich.setText("")			
				self.textInputGaebGruppe.setText("")
				self.checkboxGaeb.setCheckState(QtCore.Qt.PartiallyChecked)
			
				#self.result			= userCancelled
				#self.close()
				
			def onSet(self):
				print indexPipe
				#Zuweisung der Bezeichnungen beginnt
				Leitungsbezeichnung = form.textInputBez.text()
				Medium = form.popupMedium.currentText()
				DN = form.popupDN.currentText()
				Rohrmaterial = form.popupMaterial.currentText()
				GaebGruppe = form.textInputGaebGruppe.text()
				GaebBereich = form.textInputGaebBereich.text()	
				iw=2
				ir=0 # Laufvariable Rohr für Benennung
				ia=2
				sel = FreeCADGui.Selection.getSelection()
				
				#get the acutual selection
				indexPipeSet = []
				iPipeSet=0
				for o in sel:
					#print o.Name
					if "Pipe" in o.Name :
						iPipeSet=iPipeSet+1
						indexPipeSet.append(iPipeSet)
				

				#for obj in sel:
				for item in indexPipeSet: #loop durch alle gewählten Pipeobjecte
					print(item)
					print (indexPipeSet)
					obj=sel[item-1]
					ir = ir+1
					if not Leitungsbezeichnung =="" :
							obj.Label = Leitungsbezeichnung + "_Rohr_" + str(ir)
					if not Medium =="":
						if not hasattr(obj,"Medium"):
							obj.addProperty("App::PropertyString","Medium")
						obj.Medium = Medium 
						R = float(RohrDef["R"][RohrDef["Medium"].tolist().index(Medium)])
						G = float(RohrDef["G"][RohrDef["Medium"].tolist().index(Medium)])
						B = float(RohrDef["B"][RohrDef["Medium"].tolist().index(Medium)])
						print("color",R,G,B)
						obj.ViewObject.ShapeColor = (R/255,G/255,B/255)
						#dwire Line Anpassen 
						guiDoc.getObject(obj.Base.Name).LineColor = (R/255,G/255,B/255)
						guiDoc.getObject(obj.Base.Name).DrawStyle = u"Dashdot"
						guiDoc.getObject(obj.Base.Name).LineWidth = 4.000
						
					if not Rohrmaterial =="":		
						if not hasattr(obj,"Rohrmaterial"):
							obj.addProperty("App::PropertyString","Rohrmaterial")
						obj.Rohrmaterial =  Rohrmaterial		
					if not DN =="":						
						if not hasattr(obj,"DN"):
							obj.addProperty("App::PropertyString","DN")
						obj.DN = str(DN)
						Aussendurchmesser = DNarray["Durchmesser_mm"][[ '{:.0f}'.format(x) for x in DNarray["DN"]].index(DN)]
						obj.Diameter = Aussendurchmesser
						obj.Base.FilletRadius = Aussendurchmesser * 1.5
					if not GaebBereich =="":		
						if not hasattr(obj,"GaebBereich"):
							obj.addProperty("App::PropertyString","GaebBereich")
						obj.GaebBereich = GaebBereich 	
					if not GaebGruppe =="":		
						if not hasattr(obj,"GaebGruppe"):
							obj.addProperty("App::PropertyString","GaebGruppe")
						obj.GaebGruppe = GaebGruppe 	
					if not "PartiallyChecked" in str(form.checkboxGaeb.checkState() ): #wenn partially checked dann keine Veränderung
						if not hasattr(obj,"GaebExport"):
							obj.addProperty("App::PropertyBool","GaebExport")
						obj.GaebExport = form.GaebExport
						#print(str(form.checkbox.isChecked()))

						#AB Hier scheinbar für Armaturen todo noch durchschauen
						#ir +=2
						#print("Name: " + Leitungsbezeichnung + "_Rohr_" + str(ir))
					#	object_A = obj 
						#print(object_A.Label)
					#	for obj in sel:
					#		object_B = obj
					#		common = object_A.Shape.common( object_B.Shape )
					#		if common.Volume > 0.0 and (str(object_A.Label) <> str(object_B.Label)) and "_Rohr_" not in str(object_B.Label) :
					#			print("Ueberschneidung "+ object_A.Label +" " + object_B.Label + " Nr " + str(ia))
								#Nummer aus String entfernen und auch Leitungsbezeichnung um Anhauufung Leitunsart Name zu vermeiden
					#			object_B.Label = Leitungsbezeichnung + "_"+ filter(str.isalpha, str(str(object_B.Label).replace(Leitungsbezeichnung,'')) )+ "_" + str(ia)
								#add property geht nur bei PythonFeature objects
								#if form.checkboxGaeb.isChecked():
								#	print(str(object_B.label))
								#	object_B.addProperty("App::PropertyBool","GaebExport")
								#	object_B.GaebExport = True
					obj.touch()
				#for obj in FreeCAD.ActiveDocument.Objects:
					#obj.touch()
				FreeCAD.ActiveDocument.recompute() 

			def onupdate(self):
				self.initUI()

			def onsetSel(self):
				#todo update selectin following properties from menue	
				FreeCAD.ActiveDocument.recompute()

			def onpipeShow(self):
				if self.pipeShowButton.isChecked():
					for o in FreeCAD.ActiveDocument.Objects :
						print o.Name
						if "Pipe" in o.Name :
							obj = App.ActiveDocument.getObject(o.Name)
							#print dir(obj)
							#print o.Name
							if  not form.textInputBez.text():
								Gui.ActiveDocument.getObject(o.Name).Visibility=False						
							elif form.textInputBez.text().lower() in o.Label.lower():
								print "text"
								Gui.ActiveDocument.getObject(o.Name).Visibility=False
								
				else:
					for o in FreeCAD.ActiveDocument.Objects :
						if "Pipe" in o.Name :
							if  not form.textInputBez.text():
								Gui.ActiveDocument.getObject(o.Name).Visibility=True						
							elif form.textInputBez.text().lower() in o.Label.lower():
								print "text"
								Gui.ActiveDocument.getObject(o.Name).Visibility=True	

			def onpipeLineShow(self):
				if self.pipeShowLineButton.isChecked():
					for o in FreeCAD.ActiveDocument.Objects :
						print o.Label
						if "Pipe" in o.Name :
							obj = App.ActiveDocument.getObject(o.Base.Name)
							if  not form.textInputBez.text():
								Gui.ActiveDocument.getObject(o.Base.Name).Visibility=True						
							elif form.textInputBez.text().lower() in o.Label.lower():
								print "text"
								Gui.ActiveDocument.getObject(o.Base.Name).Visibility=True	
				else:
					for o in FreeCAD.ActiveDocument.Objects :
						print o.Label
						if "Pipe" in o.Name :
							if  not form.textInputBez.text():
								Gui.ActiveDocument.getObject(o.Base.Name).Visibility=False						
							elif form.textInputBez.text().lower() in o.Label.lower():
								print "text"
								Gui.ActiveDocument.getObject(o.Base.Name).Visibility=False	
			
		userCancelled		= "Cancelled"
		userOK			= "OK"

		form = ExampleModalGuiClass()
		form.exec_()

		if form.result==userCancelled:
			pass # steps to handle user clicking Cancel

		doc.recompute
				
class MyTool1:
	"My tool object"
	def GetResources(self):
		return {"MenuText": "My Command",
				"Accel": "Ctrl+M",
				"ToolTip": "My extraordinary command",
				"Pixmap": FreeCAD.__path__[0].encode('ascii','ignore') + "\pipeExt\icons\Example.svg"}

	def IsActive(self):
		return True #if true not grayed out

	def Activated(self):
		print("active1")
                # do something here...
FreeCADGui.addCommand('MyTool',MyTool())
FreeCADGui.addCommand('MyTool1',MyTool1())
# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui
import FreeCAD

#todo Anpassen Auswahl Reduzierung DN Anfang, DN Ende, length Anfang, lenght Ende
#Dadurch können an einem Rohrstück mehrere Reduzierungen verwendet werden
class Reduction:

	def __init__(self, obj):
		'''Add some custom properties to our box feature'''
		obj.addProperty("App::PropertyLink","Base","Component").Base =FreeCADGui.Selection.getSelection()[0]
		obj.addProperty("App::PropertyEnumeration","Position","Orientation").Position = ['Start','End']
		obj.addProperty("App::PropertyLength","Length","Orientation").Length=100
		obj.addProperty("App::PropertyLength","Diameter","Orientation").Diameter=obj.Base.Diameter/2
		obj.Proxy = self

	def execute(self, fp):
		'''"Print a short message when doing a recomputation, this method is mandatory" '''
		#print "flansch augerichtet"
		#fp.Shape = Part.makeCylinder(fp.d,20,v,r,0)
		import Part
		v0=fp.Base.Base.Shape.Vertexes[0].Point
		r0=fp.Base.Base.Shape.Vertexes[0].Point.sub(fp.Base.Base.Shape.Vertexes[1].Point)
		vE=fp.Base.Base.Shape.Vertexes[-1].Point
		rE=fp.Base.Base.Shape.Vertexes[-1].Point.sub(fp.Base.Base.Shape.Vertexes[-2].Point)
		#fp.Diameter = 
		if (fp.Position == "Start") :
			fp.Base.OffsetStart.Value = fp.Length
			fp.Base.OffsetEnd.Value = 0
			Red = Part.makeCone(fp.Base.Diameter/2,fp.Diameter/2,fp.Length,v0.sub(r0.normalize().multiply(fp.Length)),r0)
			#print "v0", v0
			#print "r0", r0
			#print "nur Startflansch"
		elif (fp.Position == "End") :
			fp.Base.OffsetEnd.Value = fp.Length
			fp.Base.OffsetStart.Value = 0
			Red = Part.makeCone(fp.Base.Diameter/2,fp.Diameter/2,fp.Length,vE.sub(rE.normalize().multiply(fp.Length)),rE)
		fp.Shape = Red
		
class ViewProviderReduction:
	def __init__(self, obj):
		''' Set this object to the proxy object of the actual view provider '''
		#obj.addProperty("App::PropertyLink","Base","Component").Base =FreeCADGui.Selection.getSelection()[0]
		obj.Proxy = self

	def getDefaultDisplayMode(self):
		''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
		#self.color = fp.Base.ViewObject.ShapeColor	
		return "Flat Lines"

	def updateData(self, fp, prop):
		'''If a property of the handled feature has changed we have the chance to handle this here'''
		# fp is the handled feature, prop is the name of the property that has changed
		#self.color = fp.Base.ViewObject.ShapeColor		
		pass
		
#the following if prevents the execution (creation) of the object when the file is only imported 
#if __name__ == '__main__': #if the module is run like a macro, this check will pass. If it's just being imported - no.
#	import Reduction #replace 'mymacro' with your macro file name, without '.py'		
#	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Reduction")
#	Reduction.Reduction(a)
#	Reduction.ViewProviderReduction(a.ViewObject)
#	App.ActiveDocument.recompute() 
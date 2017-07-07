#osuhitobjects
#from osuTypes import CurveTypes

#x,y,time,type,hitSound,addition
class Circle:
	x = None
	y = None
	hitTime = None
	hitSound = None
	addition = None
	
	def __init__(self, x, y, hitTime, hitSound = None, addition = None):
		self.x = int(x)
		self.y = int(y)
		self.hitTime = float(hitTime)
		self.hitSound = hitSound
		self.addition = addition
		#print("circle")
		
	def getPosition(self):
		return (self.x, self.y)
	
	def getTime(self):
		return self.hitTime

	
#x, y, time, type, hitSound, sliderType|curveX:curveY|...|repeat, pixelLength|edgeHitsound:edgeAddition, addition
class Slider:
	x = None
	y = None
	hitTime = None
	hitType = None
	sliderType = None #curveType
	curves = []
	repeats = None
	pixLength = None
	edgeHitsound = None
	edgeAddition = None
	def __init__(self, x, y, hitTime, sliderType, curves, repeats, pixLength, edgeHitsound = None, edgeAddition = None):
		self.x = int(x)
		self.y = int(y)
		self.hitTime = float(hitTime)
		self.sliderType = sliderType
		self.curves = curves
		self.repeats = repeats
		self.pixLength = pixLength
		self.edgeHitsound = edgeHitsound
		self.edgeAddition = edgeAddition
		#print("Slider")
		
	def getPosition(self):
		return (self.x, self.y)
	
	def getTime(self):
		return self.hitTime
		
	def getType(self):
		return self.sliderType
		
	def getCurves(self):
		return self.curves
	
	def getRepeats(self):
		return self.repeats
		
	def getLength(self):
		return self.pixLength
		

#x,y,time,type,hitSound,endTime,addition
class Spinner:
	x = None
	y = None
	hitTime = None
	hitSound = None
	endTime = None 
	addition = None
	def __init__(self, x, y, hitTime, endTime, hitSound = None, addition = None):
		self.x = int(x)
		self.y = int(y)
		self.hitTime = float(hitTime)
		self.endTime = endTime
		self.hitSound = None		
		self.addition = None
		#print("spinner")
	
	def getPosition(self):
		return (self.x, self.y)
	
	def getTime(self):
		return self.hitTime
	
	def getEnd(self):
		return self.endTime
	
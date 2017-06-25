#osuhitobjects

#x,y,time,type,hitSound,addition
class cricle:
	x = None
	y = None
	hitTime = None
	hitSound = None
	addition = None
	
	def __init__(self, x, y, hitTime, hitSound = None, addition = None):
		self.x = x
		self.y = y
		self.hitTime = hitTime
		self.hitSound = hitSound
		self.addition = addition
		print("circle")

	
#x, y, time, type, hitSound, sliderType|curveX:curveY|...|repeat, pixelLength|edgeHitsound:edgeAddition, addition
class slider:
	x = None
	y = None
	hitTime = None
	hitType = None
	sliderType = None
	curves = []
	repeats = None
	pixLength = None
	edgeHitsound = None
	edgeAddition = None
	def __init__(self, x, y, hitTime, hitType, sliderType, curves, repeats, pixLength, edgeHitsound = None, edgeAddition = None):
		self.x = x
		self.y = y
		self.hitTime = hitTime
		self.hitType = hitType
		self.sliderType = sliderType
		self.curves = curves
		self.repeats = repeats
		self.pixLength = pixLength
		self.edgeHitsound = edgeHitsound
		self.edgeAddition = edgeAddition
		print("Slider")
		

#x,y,time,type,hitSound,endTime,addition
class spinner:
	x = None
	y = None
	hitTime = None
	hitSound = None
	endTime = None 
	addition = None
	def __init__(self, x, y, hitTime, endTime, hitSound = None, addition = None):
		self.x = x
		self.y = y
		self.hitTime = hitTime
		self.endTime = endTime
		self.hitSound = None		
		self.addition = None
		print("spinner")
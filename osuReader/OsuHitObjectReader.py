import re
class cricle:
	hitType = ''
	def __init__(line):
		print("circle")
	#x,y,time,type,hitSound,addition
	#x,y,time,type,hitSound,sliderType|curveX:curveY|...|repeat,pixelLength|edgeHitsound:edgeAddition,addition
	#x,y,time,type,hitSound,endTime,addition
	
class slider:
	hitType = ''
	def __init__(line):
		print("circle")
		
class spinner:
	hitType = ''
	def __init__(line):
		print("spinner")
		
		

def read(line):
	foi = re.compile(r'(([0-9]*[.])?[0-9]+)')#float or int
	
	#x,y,time,type,hitSound,addition
	#example: 164,260,2434,1,0,0:0:0:0:
	circle = r'(\d+,){4}\d+((\d:){4})*'
	#x,y,time,type,hitSound,sliderType|curveX:curveY|...|repeat,pixelLength|edgeHitsound:edgeAddition,addition
	#example: 424,96,66,2,0,B|380:120|332:96|332:96|304:124,1,130,2|0,0:0|0:0,0:0:0:0:
	slider = r'(\d+,){5}\S(\|\d+:\d+)+,\d+,(\d+.\d+),\d+\|\d+,\d+:\d+\|\d+:\d+,(\d:){4}' 
	#x,y,time,type,hitSound,endTime,addition
	#example: 256,192,730,12,8,3983
	spinner = r'(\d+,){5}\d+]' 
	rCircle = re.compile(circle)
	rSlider = re.compile(slider)
	rSpinner = re.compile(spinner)
	if(rSlider.match(line)):
		print("s")
	elif(rCircle.match(line)):
		print("c")
	elif(rSpinner.match(line)):
		print("spinner")
	
	
	
	
	
	#THIS WORKS BUT NOT v9 FOR v13: r'(\d+,){5}(\d:){4}'
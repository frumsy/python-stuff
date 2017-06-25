import re
import osuData
		
		#x,y,time,type,hitSound,addition
	#example: 164,260,2434,1,0,0:0:0:0:

	#x,y,time,type,hitSound,sliderType|curveX:curveY|...|repeat,pixelLength|edgeHitsound:edgeAddition,addition
	#example: 424,96,66,2,0,B|380:120|332:96|332:96|304:124,1,130,2|0,0:0|0:0,0:0:0:0:
	
	#x,y,time,type,hitSound,endTime,addition
	#example: 256,192,730,12,8,3983
	
def read(line):	
	data = line.split(',')
	
	if(len(data) > 4):
		hitType = int(data[3]) & ~osuData.ColourHax
		combo = hitType == osuData.NewCombo
		print(combo)
		print(hitType)
	
	
	
	
	#THIS WORKS BUT NOT v9 FOR v13: r'(\d+,){5}(\d:){4}'
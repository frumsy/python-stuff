#Difficulty reader
import re
import osuData

def read(line):
	if(re.match(r'HPDrainRate:\d*',line)):
		osuData.difficulty['HPDrainRate'] = line.split(':')[1]			
	elif(re.match(r'CircleSize:\d*',line)):
		osuData.difficulty['CircleSize'] = line.split(':')[1]		
	elif(re.match(r'OverallDifficulty:\d*',line)):
		osuData.difficulty['OverallDifficulty'] = line.split(':')[1]		
	elif(re.match(r'ApproachRate:\d*',line)):
		osuData.difficulty['ApproachRate'] = line.split(':')[1]		
	elif(re.match(r'SliderMultiplier:\d*',line)):
		osuData.difficulty['SliderMultiplier'] = line.split(':')[1]		
	elif(re.match(r'SliderTickRate:\d*',line)):
		osuData.difficulty['SliderTickRate'] = line.split(':')[1]		
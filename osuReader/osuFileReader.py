#osu beatmap file reader
import csv
import re
import osuData
import OsuGeneralReader as generalReader
import OsuDifficultyReader as difficultyReader
import OsuMetaDataReader as metadataReader
import OsuHitObjectReader as hitObjectReader

def getLines(fileName):
	
	with open(fileName, 'rb') as csvfile:
		lines = []
		reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in reader:
			lines.append(''.join(row))
		return lines
		
def getOsuData(fileName):
	title = r'\[\S*\]' 
	rTitle = re.compile(title)
	section = 'version'	
	sections = ['[General]','[Metadata]','[Difficulty]','[HitObjects]']
	
	lines = getLines(fileName)
	for line in lines:
		#add section to get file format here
		if(rTitle.match(line)):
			section = line
			print(section)
			
		if(section == '[General]'):
			generalReader.read(line)
		elif(section == '[Metadata]'):
			metadataReader.read(line)
		elif(section == '[Difficulty]'):
			difficultyReader.read(line)
		elif(section == '[HitObjects]'):
			hitObjectReader.read(line)

getOsuData('Kozato.osu')#test.osu #Kozato.osu	
#print osuData.hitObjects



"""
def gethitObjects(filename):
	with open(filename,'r') as f:
		content = f.read()
		keyword = '[HitObjects]'
		preHitObjects, keyword, hitObjects = content.partition(keyword)
		hitObjects = hitObjects.split('\n')
		hitobjs = []
		for line in hitObjects:
			linedata = line.split(',')
			if(len(linedata) >= 4):
				if(linedata[4] == '1' or '6'):
					hitobjs.append((linedata[0],linedata[1],linedata[2],linedata[3]))
					print("circle")
				elif(linedata[4] == '2'):
					print("slider")
				else:
					print("unknown")
		return hitobjs
"""
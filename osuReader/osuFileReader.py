#osu beatmap file reader
import csv
import re
import osuData
import enumT
import OsuGeneralReader as generalReader
import OsuDifficultyReader as difficultyReader
import OsuMetaDataReader as metadataReader

def getLines(fileName):
	
	with open(fileName, 'r') as csvfile:
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
	
	hits = []
	
	lines = getLines(fileName)
	for line in lines:
		#add section to get file format here
		if(rTitle.match(line)):
			section = line
			#print(section)
			
		if(section == '[General]'):
			generalReader.read(line)
		elif(section == '[Metadata]'):
			metadataReader.read(line)
		elif(section == '[Difficulty]'):
			difficultyReader.read(line)
		elif(section == '[HitObjects]'):
			hits.append(enumT.parse(line))
			#hitObjectReader.read(line)
	return hits

#getOsuData('Station Earth - Cold Green Eyes ft. Roos Denayer (Bearizm) [Divine].osu')#test.osu #Kozato.osu	
#print("numCircles: ", osuData.numCircles)
#print("numSliders: ", osuData.numSliders)
#print("numSpinners: ", osuData.numSpinners)

#print osuData.hitObjects
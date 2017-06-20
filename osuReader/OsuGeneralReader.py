#OsuGeneralReader
import re
import osuData

def read(line):
	if(re.match(r'AudioFilename:\S*',line)):
		osuData.general['AudioFilename'] = line.split(':')[1]	
	elif(re.match(r'AudioLeadIn:\S*',line)):
		osuData.general['AudioLeadIn'] = line.split(':')[1]	
	elif(re.match(r'PreviewTime:\S*',line)):
		osuData.general['PreviewTime'] = line.split(':')[1]	
	elif(re.match(r'Countdown:\S*',line)):
		osuData.general['Countdown'] = line.split(':')[1]	
	elif(re.match(r'SampleSet:\S*',line)):
		osuData.general['SampleSet'] = line.split(':')[1]	
	elif(re.match(r'StackLeniency:\S*',line)):
		osuData.general['StackLeniency'] = line.split(':')[1]	
	elif(re.match(r'Mode:\S*',line)):
		osuData.general['Mode'] = line.split(':')[1]	
	elif(re.match(r'LetterboxInBreaks:\S*',line)):
		osuData.general['LetterboxInBreaks'] = line.split(':')[1]	
	elif(re.match(r'EpilepsyWarning:\S*',line)):
		osuData.general['EpilepsyWarning'] = line.split(':')[1]	
	elif(re.match(r'WidescreenStoryboard:\S*',line)):
		osuData.general['WidescreenStoryboard'] = line.split(':')[1]

#OsuMetaDataReader
import re
import osuData
def read(line):
	if(re.match(r'Title:\S*',line)):
		osuData.metadata['Title'] = line.split(':')[1]			
	elif(re.match(r'TitleUnicode:\S*',line)):
		osuData.metadata['TitleUnicode'] = line.split(':')[1]		
	elif(re.match(r'Artist:\S*',line)):
		osuData.metadata['Artist'] = line.split(':')[1]			
	elif(re.match(r'ArtistUnicode:\S*',line)):
		osuData.metadata['ArtistUnicode'] = line.split(':')[1]		
	elif(re.match(r'Creator:\S*',line)):
		osuData.metadata['Creator'] = line.split(':')[1]			
	elif(re.match(r'Version:\S*',line)):
		osuData.metadata['Version'] = line.split(':')[1]			
	elif(re.match(r'Source:\S*',line)):
		osuData.metadata['Source'] = line.split(':')[1]			
	elif(re.match(r'Tags:\S*',line)):
		osuData.metadata['Tags'] = line.split(':')[1]		
	elif(re.match(r'BeatmapID:\d*',line)):
		osuData.metadata['BeatmapID'] = line.split(':')[1]		
	elif(re.match(r'BeatmapSetID:\d*',line)):
		osuData.metadata['BeatmapSetID'] = line.split(':')[1]
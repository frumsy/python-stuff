#python script to read HitObjects out of osu files
#returns a list of tuples in the form (x, y, time, hit_object_type) 
#hit_object_type of 6 means new color
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
#
#print gethitObjects('workfile.osu')
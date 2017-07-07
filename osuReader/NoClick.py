#osuNoClick
from win32gui import GetWindowText, GetForegroundWindow
import sched, time
import os
import win32api, win32con
import sys
import osuFileReader
import osuData
import hitObjects
import keyboard
	
#=#=#

def find(name, path):
	print('DEBUG')
	print(name)
	print(path)
	keyWords = name.split(' ')
	for root, dirs, files in os.walk(path):
		for file in files:
			if(all(word in file for word in keyWords)):
				fullPath = os.path.join(root, file)
				print('===========================================')
				print('========= ' ,fullPath,type(fullPath))
				print('===========================================')
				return fullPath
	return 'NOT FOUND'
	

def getSong():
	while(True):
		if(len(GetWindowText(GetForegroundWindow()).split(' - ')) > 1):
				return GetWindowText(GetForegroundWindow()).split(' - ')[2]
		

def rightDown(pos):
	#print('rightDown')
	x = pos[0]
	y = pos[1]
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

def rightUp(pos):
	#print('rightUp')
	x = pos[0]
	y = pos[1]
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y,0 ,0)
	
def clicker(song):
	songPath = find(song, 'C:\\Users\\Liam\\AppData\\Local\\osu!\\Songs\\')
	hits = osuFileReader.getOsuData(songPath)
	AR = float(osuData.difficulty['ApproachRate'])
	leadIn = float(osuData.general['AudioLeadIn'])
	preview = float(osuData.general['PreviewTime'])
	#tasks = sched.scheduler(time.time, time.sleep)
	#tasks.enter(5, 1, print_time, ())
	
	hits = list(filter(lambda hit: isinstance(hit, hitObjects.Circle) or
									isinstance(hit, hitObjects.Slider)or
									isinstance(hit, hitObjects.Spinner),
									hits))
	
	hitTimes = list(map(lambda x: x.getTime(), hits))
	intervals = [j-i for i, j in zip(hitTimes[:-1], hitTimes[1:])]#get the differences between the hits
	print('Approch:', AR*0.1)
	print('preview:',preview*0.00001)
	print('lead in:',leadIn*0.001)
	
	if(leadIn > 0):
		time.sleep(leadIn * 0.001)#wait for approch to be over
	if(preview > 0):
		time.sleep(preview * 0.00001)#wait for approch to be over
	
	#keyboard.wait('s')
	print('gogogo!')
	time.sleep(AR*0.1)#wait for approch to be over	
	#for hit in hits:
	prev = 0.0
	for hit in hits: 
		if(keyboard.is_pressed('+')):
				print('Exiting')
				exit()
		delay = hit.getTime() * 0.001 - prev
		time.sleep(delay) 
		#x512 --- 1680 ==== 3.28125
		#y384 --- 1050 ==== 2.734375
		prev = hit.getTime()* 0.001
		pos = (int(3.28125 * hit.getPosition()[0]), int(2.734375 * hit.getPosition()[1]))
		win32api.SetCursorPos(pos)
		rightDown(pos)
		print('click')
		rightUp(pos)
	print('\nDone!\n')
		
while(True):
	keyboard.wait('enter')
	clicker(getSong())
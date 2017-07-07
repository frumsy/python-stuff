#osu turtple visualizer
##NEEDS TO USE PYTHON 34
import time
import turtle
import osuFileReader
import osuData
import hitObjects


llx = 0
lly = 720
urx = 1280
ury = 0
turtle.setworldcoordinates(llx, lly, urx, ury)
t = turtle.Turtle()
t.color("blue")
t.speed(speed=0)

#turtle.ontimer(fun, t=0)

hits = osuFileReader.getOsuData("kozato.osu")
prevDelay = 0.0
for hit in hits:
	if(isinstance(hit, hitObjects.Circle)):
		t.color("red")
		#print("Circle")
		delay = hit.getTime() - prevDelay
		#print('Circle debug types:::',type(prevDelay), type(hit.getTime()), type(delay))
		#print('Circle debug :::',prevDelay, hit.getTime(), delay)
		turtle.delay(delay)
		prevDelay = hit.getTime()
		t.setpos(hit.getPosition())
		turtle.update()
		
	elif(isinstance(hit, hitObjects.Slider)):
		t.color("green")
		#print('Slider')
		delay = hit.getTime() - prevDelay
		#print('Slider debug types:::',type(prevDelay), type(hit.getTime()), type(delay))
		#print('Slider debug :::',prevDelay, hit.getTime(), delay)
		turtle.delay(delay)
		prevDelay = hit.getTime()
		t.setpos(hit.getPosition())
		turtle.update()
	
	elif(isinstance(hit, hitObjects.Spinner)):
		t.color("black")
		print('Spinner')
		delay = hit.getTime() - prevDelay
		#print('Spinner debug types:::',type(prevDelay), type(hit.getTime()), type(delay))
		#print('Spinner debug :::',prevDelay, hit.getTime(), delay)
		turtle.delay(delay)
		prevDelay = hit.getTime()
		t.setpos(hit.getPosition())
		turtle.update()
	
	else:
		print("NOT HIT OBJECT: ",type(hit))
		#raise ValueError('Unknown hit object type.')
	#t.setpos(x,y)
	t.dot()
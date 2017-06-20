#osu turtple visualizer
##NEEDS TO USE PYTHON 34
import time
import turtle
import hitObjectReader as hor

llx = 0
lly = 720
urx = 1280
ury = 0
turtle.setworldcoordinates(llx, lly, urx, ury)
t = turtle.Turtle()
t.color("blue")
t.speed(speed=1)

#turtle.ontimer(fun, t=0)

hitObjects = hor.gethitObjects("test.osu")



for hits in hitObjects:
	hits = [float(obj) for obj in hits]#convert the strings to floats
	x,y,htime,htype = hits
	print(htime) 
	t.setpos(x,y)
	t.dot()
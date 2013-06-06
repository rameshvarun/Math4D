from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import PIL.Image

from vector import *
from function import *
from parametric import *
from vectorfield import *

from Tkinter import *

import Tkconstants, tkFileDialog

import os, shutil


DEFAULTSCREENSIZE = (800,600)

class Camera:
	def __init__(self):
		self.r = 20
		self.theta = 1.24
		self.phi = 0.75
		
		self.old = False
		
		self.oldTheta = 0
		self.oldPhi = 0
		
		self.downX = 0
		self.downY = 0
	def render(self):
		gluLookAt(self.x, self.y, self.z, 0, 0, 0, 0, 0, 1)
		
	def update(self, dt):
	
		if pygame.mouse.get_pressed()[0] == True and self.old == False:
			self.downX = pygame.mouse.get_pos()[0]
			self.downY = pygame.mouse.get_pos()[1]
			
			self.oldTheta = self.theta
			self.oldPhi = self.phi
			
		self.old = pygame.mouse.get_pressed()[0]
			
		if pygame.mouse.get_pressed()[0]:
			self.currX = pygame.mouse.get_pos()[0]
			self.currY = pygame.mouse.get_pos()[1]
			
			self.theta = self.oldTheta - float(self.currY - self.downY)/100
			self.phi = self.oldPhi - float(self.currX - self.downX)/100
	
		self.x = self.r*sin(self.theta)*cos(self.phi)
		self.y = self.r*sin(self.theta)*sin(self.phi)
		self.z = self.r*cos(self.theta)

def resize(size):
	width = size[0]
	height = size[1]
	
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60.0, float(width)/height, .1, 1000.)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
def axes():
	glBegin(GL_LINES)
	
	#Y axis
	glColor3f(0,255,0)
	glVertex3f(0,0,0)
	glColor3f(0,255,0)
	glVertex3f(0,10,0)
	
	#Z axis
	glColor3f(0,0,255)
	glVertex3f(0,0,0)
	glColor3f(0,0,255)
	glVertex3f(0,0,10)
	
	#X axis
	glColor3f(255,0,0)
	glVertex3f(0,0,0)
	glColor3f(255,0,0)
	glVertex3f(10,0,0)
	
	glEnd()
	
	drawText((0,10, 0), "y", 32)
	drawText((10,0, 0), "x", 32)
	drawText((0,0, 10), "z", 32)
	
def drawText(position, textString, size):     
    font = pygame.font.Font (None, size)
    textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,255))     
    textData = pygame.image.tostring(textSurface, "RGBA", True)     
    glRasterPos3d(*position)     
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
	
def graph(objects):
	pygame.init()
	
	screen = pygame.display.set_mode(DEFAULTSCREENSIZE, HWSURFACE|OPENGL|DOUBLEBUF)

	resize(DEFAULTSCREENSIZE)
	
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_FLAT)
	glClearColor(0, 0, 0, 0.0)
	glEnable (GL_BLEND);
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	
	
	clock = pygame.time.Clock()
	
	cam = Camera()
	
	u = 0
	
	running = True
	
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYUP and event.key == K_ESCAPE:
				running = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 4:
					cam.r *= 0.9
				if event.button == 5:
					cam.r *= 1.1

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		time_passed = clock.tick()
		dt = time_passed / 1000.0
		
		cam.update(dt)
		
		keys =  pygame.key.get_pressed()
		
		if keys[pygame.K_RIGHT]:
			u += dt
		if keys[pygame.K_LEFT]:
			u -= dt

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		cam.render()
		
		axes()
		drawText((0,0, 0), "U = " + str(u), 32)
		
		for obj in objects:
			obj.draw(u)

		pygame.display.flip()
		
	pygame.quit()
			
def render(objects, r=3, h=1, length=5.0, fps=25, speed=2):
	pygame.init()
	
	screen = pygame.display.set_mode(DEFAULTSCREENSIZE, HWSURFACE|OPENGL|DOUBLEBUF)

	resize(DEFAULTSCREENSIZE)
	
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_FLAT)
	glClearColor(0, 0, 0, 0.0)
	glEnable (GL_BLEND);
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	
	cam = Camera()
	cam.r = r
	
	u = 0
	
	running = True
	
	frame = 0
	
	
	while running:
	
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYUP and event.key == K_ESCAPE:
				running = False

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		time = frame/float(fps)
		cam.phi = speed*time/100

		cam.x = cam.r*sin(cam.theta)*cos(cam.phi)
		cam.y = cam.r*sin(cam.theta)*sin(cam.phi)
		cam.z = h

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		cam.render()
		
		axes()
		#drawText((0,0, 0), "U = " + str(u), 32)
		
		for obj in objects:
			obj.draw(u)
		
		
		im = PIL.Image.frombuffer("RGBA", (800, 600), glReadPixels( 0,0, 800, 600, GL_RGBA, GL_UNSIGNED_BYTE), "raw", "RGBA", 0, 0)
		im.save("out\\" + str(frame) + ".png")

		pygame.display.flip()
		
		print "Frame " + str(frame) + " rendered."
		frame += 1
		
		if frame > length*fps:
			running = False
		
	pygame.quit()
	
	try:
		os.remove("output.mp4")
	except:
		pass
		
	os.system('ffmpeg -framerate ' + str(fps) + ' -f image2 -i out//%d.png output.mp4')



from gui import *

root.title("Math4D")

root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar

menu_file = Menu(menubar)
menu_ex = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_ex, label='Examples')

currentfile = "empty"

def newFile():
	global currentfile
	currentfile = "empty"
	code.delete(1.0, END)
	
	
def openFile():
	global currentfile
	
	currentfile = tkFileDialog.askopenfilename()
	file = open(currentfile)
	code.delete(1.0, END)
	
	for line in file.readlines():
		code.insert(END, line)
		
	file.close()
		
def saveFile():
	global currentfile
	
	file = None
	
	if currentfile == "empty":
		currentfile = tkFileDialog.asksaveasfilename()
		
	file = open(currentfile, "w")
	file.write(code.get(1.0, END))
	file.close()
	
	
def closeFile():
	sys.exit(0)
	
def runCode():
	lines = code.get(1.0, END).splitlines()
	for line in lines:
		if len(line.split()) > 0:
			exec(line)

menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Open', command=openFile)
menu_file.add_command(label='Save', command=saveFile)
menu_file.add_command(label='Close', command=closeFile)

from examples import *


code.pack()

for example in examples:
	menu_ex.add_command(label=example.name, command=example.set)



b = Button(root, text="Run", command=runCode)
b.pack()

root.mainloop()
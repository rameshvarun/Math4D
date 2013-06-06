from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

class Vector:
	def __init__(self, name, data):
		self.name = name
		self.data = data
		self.dimensions = len(self.data)
		
		self.color = (255,255,255)
		
	def draw(self, u):
		glBegin(GL_LINES)
		
		if self.dimensions == 1:
			#Y axis
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(0,0,0)
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(self.data[0],0, 0)
			
		if self.dimensions == 2:
			#Y axis
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(0,0,0)
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(self.data[0],self.data[1], 0)
			
		if self.dimensions == 3:
			#Y axis
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(0,0,0)
			glColor3f(self.color[0],self.color[1],self.color[2])
			glVertex3f(self.data[0],self.data[1], self.data[2])
			
		glEnd()
		
		if self.dimensions == 4:
			glBegin(GL_POINTS)
			
			if (u <= self.data[3] and u >= 0) or (u >= self.data[3] and u <= 0):
				ratio = abs(u/self.data[3])
				
				glColor3f(self.color[0],self.color[1],self.color[2])
				glVertex3f(self.data[0]*ratio,self.data[1]*ratio, self.data[2]*ratio)
			
			glEnd()
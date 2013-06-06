from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

def normalize(vector):
	mag = 0
	for value in vector:
		mag += value*value
		
	mag = sqrt(mag)
	
	if mag == 0:
		return vector
	
	newvector = []
	
	for value in vector:
		newvector.append(value/mag)
		
	return newvector

class VectorField:
	def __init__(self, name, data, dimensions):
		self.name = name
		self.data = data
		
		self.color = (255,255,255)
		self.lowx = -5
		self.highx = 5
		
		self.lowy = -5
		self.highy = 5
		
		self.lowz = -5
		self.highz = 5
		
		self.step = 1
		self.dimensions = dimensions
		
	def eval(self, x = 0, y = 0, z = 0, u = 0):
		output = []
		
		for eq in self.data:
			output.append(eval(eq))
		
		return output
		
	def draw(self, u):
	
		keys =  pygame.key.get_pressed()
		
		if keys[pygame.K_1]:
			self.step = 1
		if keys[pygame.K_2]:
			self.step = 0.5
			
		if self.dimensions == 1:
			glBegin(GL_LINES)
			
			x = self.lowx
			while x < self.highx:
				vector = normalize(self.eval(x))
				
				
				glColor3f(self.color[0],self.color[1],self.color[2])
				glVertex3f(x,0,0)
				
				if len(vector) == 1:
					glVertex3f(x + vector[0], 0, 0)
				if len(vector) == 2:
					glVertex3f(x + vector[0], vector[1], 0)
				if len(vector) == 3:
					glVertex3f(x + vector[0], vector[1], vector[2])
					
				x += self.step
			glEnd()
			
		if self.dimensions == 2:
			glBegin(GL_LINES)
			
			x = self.lowx
			while x < self.highx:
				y = self.lowy
				
				while y < self.highy:
					vector = normalize(self.eval(x, y))
					
					glColor3f(self.color[0],self.color[1],self.color[2])
					glVertex3f(x,y,0)
					
					if len(vector) == 1:
						glVertex3f(x + vector[0], y, 0)
					if len(vector) == 2:
						glVertex3f(x + vector[0], y + vector[1], 0)
					if len(vector) == 3:
						glVertex3f(x + vector[0], y + vector[1], vector[2])
						
					y += self.step
						
				x += self.step
			glEnd()
			
		if self.dimensions == 3 or self.dimensions == 4:
			glBegin(GL_LINES)
			
			x = self.lowx
			while x < self.highx:
				y = self.lowy
				
				while y < self.highy:
				
					z = self.lowz
					
					while z < self.highz:
						vector = normalize(self.eval(x , y, z, u))
						
						glColor3f(self.color[0],self.color[1],self.color[2])
						glVertex3f(x,y,z)
						
						if len(vector) == 1:
							glVertex3f(x + vector[0], y, z)
						if len(vector) == 2:
							glVertex3f(x + vector[0], y + vector[1], z)
						if len(vector) == 3:
							glVertex3f(x + vector[0], y + vector[1], z + vector[2])
							
						z += self.step
						
					y += self.step
						
				x += self.step
			glEnd()
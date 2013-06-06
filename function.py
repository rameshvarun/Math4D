from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

class Function:
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
		return eval(self.data)
		
	def draw(self, u):
	
		keys =  pygame.key.get_pressed()
		
		if keys[pygame.K_1]:
			self.step = 1
		if keys[pygame.K_2]:
			self.step = 0.5
			
		if self.dimensions == 1:
			glBegin(GL_LINES)
			
			i = self.lowx
			while i < self.highx:
				start = self.eval(i) #eval(self.data)

				end = self.eval(i + self.step) #eval(self.data)
				
				glColor3f(self.color[0],self.color[1],self.color[2])
				glVertex3f(i,0,start)
				glColor3f(self.color[0],self.color[1],self.color[2])
				glVertex3f(i+self.step, 0, end)
				
				i += self.step
			glEnd()
		
		if self.dimensions == 2:
			glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );
			
			y = self.lowy
			while y < self.highy:
				glBegin(GL_TRIANGLE_STRIP)
				
				x = self.lowx
				while x < self.highx:
					glColor3f(self.color[0],self.color[1],self.color[2])
					glVertex3f( x, y, self.eval(x,y) )
					glVertex3f( x, y + self.step, self.eval(x,y + self.step) )
					
					x += self.step
				
				glEnd()
				
				y += self.step
				
			glPolygonMode( GL_FRONT_AND_BACK, GL_FILL );
			
		if self.dimensions == 3 or self.dimensions == 4:
			glDisable(GL_DEPTH_TEST);
			glBegin(GL_QUADS);

			y = self.lowy
			while y < self.highy:

				x = self.lowx
				while x < self.highx:
					
					z = self.lowz
					while z < self.highz:
						color = (self.eval(x + self.step/2, y + self.step/2, z + self.step/2, u) / 10.0) *pow(self.step,2)
						
						if color > 1:
							color = 1
							
						if color > 0:
							glColor4f(1.0, 1.0, 1.0, color)
						
							#Front Face
							glNormal3f( 0.0, 0.0, 1.0)
							glVertex3f(x, y,  z + self.step)
							glVertex3f(x + self.step, y,  z + self.step)
							glVertex3f(x + self.step,  y + self.step,  z + self.step)
							glVertex3f(x,  y + self.step,  z + self.step)
							
							#Back Face
							glNormal3f( 0.0, 0.0,-1.0)
							glVertex3f(x, y, z)
							glVertex3f(x, y + self.step, z)
							glVertex3f(x +  self.step, y + self.step, z)
							glVertex3f( x + self.step, y, z)
							
							#Top Face
							glNormal3f( 0.0, 1.0, 0.0)
							glVertex3f(x, y+ self.step, z)
							glVertex3f(x, y+ self.step, z+ self.step)
							glVertex3f( x+self.step,  y+self.step,  z+self.step)
							glVertex3f(x+ self.step,  y+self.step, z)
							
							#Bottom Face
							glNormal3f( 0.0,-1.0, 0.0)
							glVertex3f(x+0, y+0, z+0)
							glVertex3f(x+ self.step, y+0, z+0)
							glVertex3f(x+ self.step, y+0,  z+self.step)
							glVertex3f(x+0, y+0,  z+self.step)
							
							#Right Face
							glNormal3f( 1.0, 0.0, 0.0)
							glVertex3f(x+ self.step, y+0, z+0)
							glVertex3f(x+ self.step, y+ self.step, z+0)
							glVertex3f(x+ self.step, y+ self.step,  z+self.step)
							glVertex3f(x+ self.step, y+0, z+ self.step)
							
							#Left Face
							glNormal3f(-1.0, 0.0, 0.0)
							glVertex3f(x+0, y+0, z+0)
							glVertex3f(x+0, y+0,  z+self.step)
							glVertex3f(x+0,  y+self.step, z+ self.step)
							glVertex3f(x+0,  y+self.step,z+ 0)
						
						z += self.step
					
					x += self.step
				y += self.step
			
			glEnd()
			glEnable(GL_DEPTH_TEST);
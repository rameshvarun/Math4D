from math import *

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

class Parametric:
	def __init__(self, name, data, variables):
		self.name = name
		self.data = data
		
		self.color = (255,255,255)
		self.lowt = -10
		self.hight = 10
		
		self.lowr = -10
		self.highr = 10
		
		self.lows = -10
		self.highs = 10
		
		self.stept = 1
		self.stepr = 1
		self.steps = 1
		
		self.dimensions = variables
		
	def eval(self, t = 0, r = 0, s = 0):
		output = []
		
		for eq in self.data:
			output.append(eval(eq))
		
		return output
		
	def table(self, variable = 't', t = 0, r = 0, s = 0):
		print "x, y, z"
		if variable == 't':
			t = self.lowt
			while t < self.hight:
				point = self.eval(t, r, s)
				
				print str(point[0]) + ", " + str(point[1]) + ", " + str(point[2])
				
				t += self.stept
			
			point = self.eval(self.hight, r, s)
			
			print str(point[0]) + ", " + str(point[1]) + ", " + str(point[2])
			
	def draw(self, u):
	
		keys =  pygame.key.get_pressed()
		
		if keys[pygame.K_1]:
			self.step = 1
		if keys[pygame.K_2]:
			self.step = 0.5
		if keys[pygame.K_3]:
			self.step = 0.1
			
		if self.dimensions == 1:
			glBegin(GL_LINES)
			
			t = self.lowt
			while t < self.hight:
				start = self.eval(t)
				
				end = self.eval(t + self.stept)
				if t + self.stept > self.hight:
					end = self.eval(self.hight)
				
				glColor3f(self.color[0],self.color[1],self.color[2])
				
				if len(start) == 1:
					glVertex3f(start[0],0,0)
					glVertex3f(end[0], 0, 0)
				if len(start) == 2:
					glVertex3f(start[0],start[1],0)
					glVertex3f(end[0], end[1], 0)
				if len(start) == 3:
					glVertex3f(start[0],start[1],start[2])
					glVertex3f(end[0], end[1], end[2])
					
				t += self.stept
			glEnd()
			
		if self.dimensions == 2:
			glBegin(GL_POINTS)
			
			trange = []
			
			t = self.lowt
			while t < self.hight:
				trange.append(t)
				
				t += self.stept
				
			trange.append(self.hight)
			
			rrange = []
			
			r = self.lowr
			while r < self.highr:
				rrange.append(r)
				
				r += self.stepr
				
			rrange.append(self.highr)
			
			for t in trange:
				for r in rrange:
					pos = self.eval(t,r)
					glColor3f(self.color[0],self.color[1],self.color[2])
					
					glVertex3f(pos[0],pos[1],pos[2])
			'''
			t = self.lowt
			while t < self.hight:
				r = self.lowr
				
				while r < self.highr:
					pos = self.eval(t,r)
					
					glColor3f(self.color[0],self.color[1],self.color[2])
					glVertex3f(pos[0],pos[1],pos[2])
					
					r += self.stepr
					
				t += self.stept
			'''
			
			glEnd()
			
		if self.dimensions == 3:
			glBegin(GL_POINTS)
			
			t = self.lowt
			while t < self.hight:
				r = self.lowr
				
				while r < self.highr:
				
					s = self.lows
					
					while s < self.highs:
						pos = self.eval(t,r,s)
						
						glColor3f(self.color[0],self.color[1],self.color[2])
						glVertex3f(pos[0],pos[1],pos[2])
						
						s += self.steps
						
					r += self.stepr
					
				t += self.stept
			glEnd()
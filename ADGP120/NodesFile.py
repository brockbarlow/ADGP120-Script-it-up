import pygame #using pygame
from pygame import * #import everything

class Node(object): #node class. used to create node objects
	def __init__(self, x, y): #init function. used to setup variables
		self.x = x #x value
		self.y = y #y value
		self.f = None #g + h
		self.g = None #movement cost
		self.h = None #manhatton cost
		self.parent = None #current node
		self.walkable = True #if walkable or not
		self.color = (255,255,255) #white color value
		self.height = 20 #size of grid (up to down)
		self.width = 20 #size of grid (left to right)
		self.margin = 5 #space between the blocks
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2)) #used for path line
		
	def draw(self, screen): #draw function
		c = self.color if (self.walkable) else (255,0,0) #walkable = white, unwalkable = red
		pygame.draw.rect(screen, c, (self.x, self.y, self.width, self.height)) #used to generate grid
		
	def setG(self, value): #function that sets and returns g value
		self.g = value #g becomes value
		self.f = self.getF() #f equals getF value
		return self.g #return g
		
	def setH(self, value): #function that sets and returns h value
		self.h = value #h becomes value
		self.f = self.getF() #f equals getF value
		return self.h #return h
		
	def getF(self): #function that returns the sum of g and h
		if self.g == None: #if g is NULL...
			self.g = 0 #g's value is/becomes zero
		if self.h == None: #if h is NULL...
			self.h = 0 #h's value is/becomes zero
		self.f = self.g + self.h #f equals sum
		return self.f #return sum
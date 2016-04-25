import pygame
from pygame import *

class Node(object):
	def __init__(self, x, y):
		self.x = x #x value
		self.y = y #y value
		self.f = None #g + h
		self.g = None #movement cost
		self.h = None #guess movement cost
		self.parent = None #current node
		self.walkable = True #if walkable or not
		self.color = (255,255,255) #walkable path color
		self.height = 20 #size of grid
		self.width = 20 #size of grid
		self.margin = 5 #space between the blocks
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2)) #used for path line
		
	def draw(self, screen): #this will draw the grid
		c = self.color if (self.walkable) else (255,0,0) #walkable = white, unwalkable = red
		pygame.draw.rect(screen, c, (self.x, self.y, self.width, self.height))
		
	def setG(self, value): #set movement cost.
		self.g = value
		return self.g
		
	def setH(self, value): #set manhatton cost.
		self.h = value
		return self.h
		
	def getF(self): #add g and h, then return that value.
		if (self.g == None) and (self.h == None):
			self.g = 0
			self.h = 0
		return self.g + self.h
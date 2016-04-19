import pygame
from pygame.locals import *

class Node(object):
	def __init__(self, x, y):
		self.f = None #movement cost plus estimated cost
		self.g = None #movement cost, None = NULL
		self.h = None #estimated cost, None = NULL
		self.width = 20
		self.height = 20
		self.margin = 5
		#self.x = x
		#self.y = y
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.position = (x, self.height - y)
		self.walkable = True
		self.parent = None
		self.color = [255,255,255]
		
	def draw(self, screen, color):
		margin = self.margin
		color = [0,0,255] if (self.walkable) else [255,0,0]
		pygame.draw.rect(screen, color, [(self.left, self.top), (self.width, self.height)])
	
	def getF(self):
		return self.g + self.h
	
	def setWalk(self, walkable):
		self.walkable = walkable
		
	def setG(self, value):
		self.g = value
		
	def setH(self, value):
		self.h = value
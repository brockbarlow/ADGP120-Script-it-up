import pygame
from pygame.locals import *

class Node:
	def __init__(self, x, y):
		self.f = None #movement cost plus estimated cost
		self.g = None #movement cost, None = NULL
		self.h = None #estimated cost, None = NULL
		self.width = None
		self.height = None
		self.margin = None
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.position = (x, self.height - y)
		self.walkable = True
		self.parent = None
		self.color = [255,255,255]
		
	def draw(self, screen, color):
		margin = self.margin
		color = [0,0,255] if (self.walkable) else [255,0,0]
		pygame.draw.rect(screen, color, [self.left, self.top, self.width, self.height])
	
	def getF(self):
		return self.h + self.g
	
	def setWalk(self, walkable):
		self.walkable = walkable
		
	def setG(self, val):
		self.g = val
		
	def setH(self, val):
		self.h = val
		
	def setWidth(self):
		self.width = 20
		
	def setHeight(self):
		self.height = 20
		
	def setMargin(self):
		self.margin = 5
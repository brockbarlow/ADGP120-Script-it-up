import pygame as gfx

class Node(object):
	def __init__(self, x, y):
		self.fCost = None
		self.gCost = None 
		self.hCost = None 
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.position = (x, self.height - y)
		self.walkable = True
		self.parent = None
		self.color = (255,255,255)
		self.adjacent = []
	
	def draw(self, screen, color):
		margin = self.margin
		color = (0,0,255) if (self.walkable) else (255,0,0)
		gfx.draw.rect(screen, color, (self.left, self.top, self.width, self.height))
	
	def getFCost(self):
		return self.gCost + self.hCost
		
	def getGCost(self, value):
		self.gCost = value
		
	def getHCost(self, value):
		self.hCost = value
	
	def setWalk(self, walkable):
		self.walkable = walkable
	
	def addAdjacent(self, value):
		self.adjacent.append(value)
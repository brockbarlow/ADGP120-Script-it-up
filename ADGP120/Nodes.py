import pygame as gfx #instead of using pygame, gfx will be used

class Node(object): #this class is used for nodes
	def __init__(self, x, y): #init function
		self.fCost = None #movement + estimated cost. None = NULL
		self.gCost = None #movement cost. None = NULL
		self.hCost = None #estimated cost. None = NULL
		self.parent = None
		self.walkable = True
		self.color = (255,255,255)
		self.width = 20 #size of grid
		self.height = 20 #size of grid
		self.margin = 5 #distance between each block in grid
		self.left = (self.margin + self.width) * x + self.margin #this is x
		self.top = (self.margin + self.height) * y + self.margin #this is y
		self.position = (x, self.height - y)
	
	def draw(self, screen, color): #draw function. used to draw the grid
		margin = self.margin
		color = self.color if (self.walkable) else (255,0,0) #good blocks are white, bad blocks are red
		gfx.draw.rect(screen, color, (self.left, self.top, self.width, self.height))
	
	def getFCost(self): #get function. gets the f cost
		return self.gCost + self.hCost
		
	def setGCost(self, value): #set function. sets the cost of g
		self.gCost = value
		
	def setHCost(self, value): #set function. sets the cost of h
		self.hCost = value
	
	def setWalk(self, walkable): #set function. sets the walkable variable
		self.walkable = walkable
	
	#self.adjacent = []
	#def addAdjacent(self, value):
		#self.adjacent.append(value)
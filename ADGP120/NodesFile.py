import pygame #using pygame
from pygame import * #import everything

class Node(object): #node class
	def __init__(self, x, y): #init function
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
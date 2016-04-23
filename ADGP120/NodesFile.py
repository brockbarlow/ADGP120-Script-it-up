import pygame
from pygame import *

class Node(object):
	def __init__(self, x, y):
		self.f = None #g + h
		self.g = None #movement cost
		self.h = None #guess movement cost
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2))
		self.left = (self.margin + self.width) * x + self.margin
		self.top = (self.margin + self.height) * y + self.margin
		self.position = (x, self.height - y)
		self.parent = None
		self.walkable = True 
		self.color = (255,255,255)
		self.x = x
		self.y = y
		self.height = 20
		self.width = 20
		self.margin = 5
		
	def draw(self, screen):
		margin = self.margin
		c = self.color if (self.walkable) else (255,0,0)
		pygame.draw.rect(screen, c, (self.x, self.y, self.width, self.height))
		
	def setG(self, value): #set movement cost.
		self.g = value
		
	def setH(self, value): #set guess movement cost.
		self.h = value
		
	def getF(self): #add g and h, then return that value.
		return self.g + self.h
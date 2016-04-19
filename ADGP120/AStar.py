import Nodes
from Nodes import *
import pygame
from pygame.locals import *

class AStar(object):
	def __init__(self, searchSpace, start, goal):
		self.open[]
		self.close[]
		self.startNode = start
		self.goalNode = goal
		self.searchNodes = searchSpace
		
	def draw(self, screen, startColor, goalColor):
		startColor = [0,255,255]
		goalColor = [0,255,0]
		pygame.draw.rect(screen, startColor, [(self.startNode.left, self.startNode.top), (self.startNode.width, self.startNode.height)])
		pygame.draw.rect(screen, goalColor, [(self.goalNode.left, self.goalNode.top), (self.goalNode.width, self.goalNode.height)])
		
	def run(self):
		self.open.append(start)
		while not self.open:
			current = self.lowestF(self.open)
		
	def lowestF(self, nodes):
		lowestF = -1
		nodeWithLowestF = None
		for node in nodes:
			if (node.f > lowestF):
				lowestF = node.f
				nodeWithLowestF = node
		return nodeWithLowestF
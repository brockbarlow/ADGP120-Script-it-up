import Nodes
from Nodes import *
import pygame
from pygame.locals import *

class AStar:
	def __init__(self, searchSpace, start, goal):
		self.open = []
		self.close = []
		
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
import Nodes
from Nodes import *

class AStar(object):
	def __init__(self, searchSpace, start, goal):
		self.open([])
		self.close([])
		self.startNode = start
		self.goalNode = goal
		self.searchNodes = searchSpace
		
	def draw(self, screen, startColor, goalColor):
		startColor = (0,255,255)
		goalColor = (0,255,0)
		gfx.draw.rect(screen, startColor, (self.startNode.x, self.startNode.y, self.startNode.width, self.startNode.height))
		gfx.draw.rect(screen, goalColor, (self.goalNode.left, self.goalNode.top, self.goalNode.width, self.goalNode.height))
		
	def run(self):
		self.open.append(start)
		while not self.open:
			current = self.lowestF(self.open)
		
	def addNodes(self, start):
		self.open.append(self.start)
		
	def lowestF(self, nodes):
		lowestF = None
		for node in nodes:
			if (lowestF == None or node.getF() < lowestF.getF()):
				lowestF = node
		for node in Nodes:
			print node.getF()
		return lowestF
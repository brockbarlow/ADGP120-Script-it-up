import NodesFile
from NodesFile import *

class AStar(object):
	def __init__(self, start, goal, searchSpace):
		self.OPENList = []
		self.CLOSEList = []
		self.ADJACENTList = []
		self.start = start
		self.current = start
		self.goal = goal
		self.searchSpace = searchSpace
		self.startColor = (255,255,0)
		self.goalColor = (0,255,0)
		self.lowestF = None
		
	def draw(self, screen):
		cStart = self.startColor
		cGoal = self.goalColor
		pygame.draw.rect(screen, cStart, (self.start.x, self.start.y, self.start.width, self.start.height))
		pygame.draw.rect(screen, cGoal, (self.goal.x, self.goal.y, self.goal.width, self.goal.height))
		
	def run(self): #run function.
		self.OPENList.append(self.start) #add start to the open list
		while not self.OPENList:
			self.current = self.lowestF(self.OPENList)
		
	def locateAdjacent(self):
		ADJACENTList = self.ADJACENTList
		for a,nodes in enumerate(self.searchSpace):
			for b,node in enumerate(nodes):
				if node == self.current:
					position = (b, a)
		
	def lowestFCost(self, nodes): #lowest f cost function. used to fine lowest f
		lowestF = self.lowestF
		for n in nodes: #for setting lowestF. if its none or greater than n, it becomes n
			if (lowestF == None or n.f < lowestF.f):
				lowestF = n
		return lowestF
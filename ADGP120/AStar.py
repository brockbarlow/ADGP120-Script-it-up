import NodesFile #AStar implements NodesFile.py
from NodesFile import *

class AStar(object):
	def __init__(self, searchSpace, start, goal):
		self.OPENList([])
		self.CLOSEList([])
		self.ADJACENTList([])
		self.start = start
		self.current = start
		self.currentColor = (0,255,255)
		self.goal = goal
		self.goalColor = (0,255,0)
		self.searchSpace = searchSpace
		self.lowestF = None
		
	def draw(self, screen, color):
		margin = self.margin
		color = self.currentColor if (self.current) else (200,100,175)
		color = self.goalColor if (self.goal) else (175,100,200)
		gfx.draw.rect(screen, color, (self.current.left, self.current.top, self.current.width, self.current.height))
		gfx.draw.rect(screen, color, (self.goal.left, self.goal.top, self.goal.width, self.goal.height))
		
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
		
		
	def lowestFCost(self, Nodes): #lowest f cost function. used to fine lowest f
		lowestF = self.lowestF
		for n in Nodes: #for setting lowestF. if its none of greater than n, it becomes n
			if (lowestF == None or n.getF() < lowestF.getF()):
				lowestF = n
		for a,nodes in enumerate(self.searchSpace): #for finding the current node
			for b,node in enumerate(nodes): #if node equals lowestF, the position will change
				if node == lowestF:
					position = (b, a)
		self.OPENList.sort() #sort the open list
		return lowestF
		
	#enumerate() is one of the built-in Python functions. It returns an enumerate object.
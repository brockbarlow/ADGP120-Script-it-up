import NodesFile #AStar implements Nodes.py
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
		color = self.currentColor if (self.current) else (0,255,255)
		color = self.goalColor if (self.goal) else (0,255,0)
		gfx.draw.rect(screen, color, (self.current.left, self.current.top, self.current.width, self.current.height))
		gfx.draw.rect(screen, color, (self.goal.left, self.goal.top, self.goal.width, self.goal.height))
		
	def run(self):
		self.OPENList.append(self.start)
		while not self.OPENList:
			self.current = self.lowestF(self.OPENList)
		
	def lowestFCost(self, Nodes):
		lowestF = self.lowestF
		for n in Nodes:
			if (lowestF == None or n.getF() < lowestF.getF()):
				lowestF = n
		
		self.OPENList.sort()
		return lowestF
		
	#def addNodes(self, start):
		#self.open.append(self.start)
	#for node in Nodes:
			#print node.getF()
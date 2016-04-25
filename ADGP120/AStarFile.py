import pygame, NodesFile
from pygame import *
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
		#self.x = x
		#self.y = y
		self.startColor = (255,255,0)
		self.goalColor = (0,255,0)
		self.pathColor = (0,0,0)
		self.lowestF = None
		self.hCost = None
		self.gCost = None
		
	def draw(self, screen):
		#margin = self.margin
		node = self.goal
		cStart = self.startColor
		cGoal = self.goalColor
		cPath = self.pathColor
		pygame.draw.rect(screen, cStart, (self.start.x, self.start.y, self.start.width, self.start.height))
		pygame.draw.rect(screen, cGoal, (self.goal.x, self.goal.y, self.goal.width, self.goal.height))
		while (node.parent != None):
			pygame.draw.line(screen, cPath, node.center, node.parent.center, 5)
			node = node.parent
		
	def startSetup(self, screen): 
		self.current = self.start
		self.current.g = 0
		self.current.h = 0
		self.current.g = self.getGCost(self.current, self.goal)
		self.current.h = self.getHCost(self.current, self.goal)
		self.OPENList.append(self.current) 
		while self.current in self.OPENList:
			adjacent = self.locateAdjacent(screen)
			for a in adjacent:
				if (a.walkable == True):
					a.parent = self.current
					a.g = self.getGCost(a, self.current)
					a.h = self.getHCost(a, self.goal)
					self.OPENList.append(a)
			self.OPENList.remove(self.current)
			self.CLOSEList.append(self.current)
			
	def run(self, screen):
		self.startSetup(screen)
		while (len(self.OPENList) > 0):
			self.current = self.lowestFCost(self.OPENList)
			self.OPENList.remove(self.current)
			self.CLOSEList.append(self.current)
			adjacentNode = self.locateAdjacent(screen)
			for a in adjacentNode:
				if (a not in self.CLOSEList):
					if (a not in self.OPENList):
						if (self.current == self.goal):
							return True
						else:
							self.OPENList.append(a)
							a.parent = self.current
							a.g = self.getGCost(a, self.current)
							a.h = self.getHCost(a, self.goal)
					else:
						travelCost = self.current.g + self.current.parent.g
						if (travelCost < a.g):
							a.parent = self.current
							a.g = travelCost
							self.OPENList.sort(key = lambda x : x.f)
		return False
		
	def locateAdjacent(self, screen):
		ADJACENTList = self.ADJACENTList
		for a,nodes in enumerate(self.searchSpace): #get current
			for b,node in enumerate(nodes):
				if node == self.current:
					position = (b, a)
		for a,nodes in enumerate(self.searchSpace): #get adjacents
			if (position[1] - 1 <= a <= position[1] + 1) and (a != None):
				for b,node in enumerate(nodes):
					if (position[0] - 1 <= b <= position[0] + 1) and (b != None) and (self.searchSpace[a][b].walkable == True) and (self.searchSpace[a][b] != self.current):
						ADJACENTList.append(self.searchSpace[a][b])
		return ADJACENTList
		
	def lowestFCost(self, nodes): #lowest f cost function. used to fine lowest f
		lowestF = self.lowestF
		for n in nodes: #for setting lowestF. if its none or greater than n, it becomes n
			if (lowestF == None) or (n.f < lowestF.f):
				lowestF = n
		return lowestF
		
	def getHCost(self, node1, node2):
		hCost = self.hCost
		for a,nodes in enumerate(self.searchSpace): #get current
			for b,node in enumerate(nodes):
				if (self.searchSpace[a][b] == node1):
					position1 = [a,b]
				if (self.searchSpace[a][b] == node2):
					position2 = [a,b]
		distance = [abs(position1[0] - position2[0]), abs(position1[1] - position2[1])]
		while (distance != [0,0]):
			if (distance[0] > 0):
				hCost += 10
				distance[0] -= 1
			if (distance[1] > 0):
				hCost += 10
				distance[1] -= 1
		return hCost
		
	def getGCost(self, node1, node2):
		gCost = self.gCost
		for a,nodes in enumerate(self.searchSpace): #get current
			for b,node in enumerate(nodes):
				if (self.searchSpace[a][b] == node1):
					position1 = [a,b]
				if (self.searchSpace[a][b] == node2):
					position2 = [a,b]
		distance = [abs(position1[0] - position2[0]), abs(position1[1] - position2[1])]
		if (distance[0] > 0) and (distance[1] > 0):
			gCost = 14
		else:
			gCost = 10
		return gCost
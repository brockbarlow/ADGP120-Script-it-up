import pygame, NodesFile #using pygame and NodesFile
from pygame import * #import everything
from NodesFile import * #import everything

class AStar(object): #astar class
	def __init__(self, start, searchSpace, goal): #init function
		self.OPENList = [] #holds possible paths
		self.CLOSEList = [] #when calculations are done, add to this list
		self.ADJACENTList = [] #nodes that surround the current node
		self.start = start #start node
		self.current = start #starts as start node
		self.goal = goal #end node
		self.searchSpace = searchSpace #search range
		self.startColor = (255,255,0) #yellow color value
		self.goalColor = (0,255,0) #green color value
		self.pathColor = (255,0,255) #purple color value
		self.adjacentColor = (0,255,255) #teal color value
		self.lowestF = None #what the lowest f is
		self.hCost = 0 #what the h cost is
		self.gCost = None #what the g cost is
		
	def draw(self, screen): #draws start and goal nodes
		cStart = self.startColor
		cGoal = self.goalColor
		pygame.draw.rect(screen, cStart, (self.start.x, self.start.y, self.start.width, self.start.height))
		pygame.draw.rect(screen, cGoal, (self.goal.x, self.goal.y, self.goal.width, self.goal.height))
		
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
		
	def locateAdjacent(self, screen): #function that finds current node adjacents
		ADJACENTList = self.ADJACENTList
		for a,nodes in enumerate(self.searchSpace): #get current node
			for b,node in enumerate(nodes):
				if node == self.current:
					position = (b, a)
		for a,nodes in enumerate(self.searchSpace): #get adjacent nodes
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
		
	def getHCost(self, node1, node2): #calculates h
		hCost = self.hCost
		for a,nodes in enumerate(self.searchSpace): #these for loops get the current node
			for b,node in enumerate(nodes):
				if (self.searchSpace[a][b] == node1): #rows
					row = [a,b]
				if (self.searchSpace[a][b] == node2): #columns
					column = [a,b]
		distance = [abs(row[0] - column[0]), abs(row[1] - column[1])]
		while (distance != [0,0]): #while first and second values do not = 0...
			if (distance[0] > 0): #if first value is greater than 0...
				hCost += 10
				distance[0] -= 1
			if (distance[1] > 0): #if second value is greater than 0...
				hCost += 10
				distance[1] -= 1
		return hCost
		
	def getGCost(self, node1, node2): #calculates g
		gCost = self.gCost
		for a,nodes in enumerate(self.searchSpace): #these for loops get the current node
			for b,node in enumerate(nodes):
				if (self.searchSpace[a][b] == node1): #rows
					row = [a,b]
				if (self.searchSpace[a][b] == node2): #columns
					column = [a,b]
		distance = [abs(row[0] - column[0]), abs(row[1] - column[1])]
		if (distance[0] > 0) and (distance[1] > 0): #if first value and second value both are greater than 0...
			gCost = 14
		else:
			gCost = 10
		return gCost
		
	def drawPath(self, screen): #draws the path from goal to start
		node = self.goal
		cPath = self.pathColor
		while (node.parent != None):
			pygame.draw.line(screen, cPath, node.center, node.parent.center, 5)
			node = node.parent
import pygame, NodesFile, math #using pygame, NodesFile and math
from pygame import * #import everything
from NodesFile import * #import everything
from math import * #import everything

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
		self.lowestF = None #what the lowest f is
		self.hCost = 0 #what the h cost is
		self.gCost = 0 #what the g cost is
		
	def draw(self, screen): #draws start and goal nodes
		cStart = self.startColor
		cGoal = self.goalColor
		pygame.draw.rect(screen, cStart, (self.start.x, self.start.y, self.start.width, self.start.height))
		pygame.draw.rect(screen, cGoal, (self.goal.x, self.goal.y, self.goal.width, self.goal.height))
		
	def startSetup(self):
		self.current = self.start
		self.OPENList.append(self.current) 
		adjacent = self.locateAdjacent()
		for a in adjacent:
			if (a.walkable == True):
				a.parent = self.current
				a.g = self.getGCost(a, self.current)
				a.h = self.getHCost(a, self.goal)
				self.OPENList.append(a)
		self.OPENList.remove(self.current)
		self.CLOSEList.append(self.current)
			
	def run(self):
		self.startSetup()
		while (len(self.OPENList) > 0):
			self.current = self.lowestFCost(self.OPENList)
			self.OPENList.remove(self.current)
			self.CLOSEList.append(self.current)
			adjacentNode = self.locateAdjacent()
			for a in adjacentNode:
				if (a not in self.CLOSEList):
					if (a not in self.OPENList):
						if (self.goal in self.OPENList) or (self.current == self.goal):
							return True
						else:
							a.parent = self.current
							a.g = self.getGCost(a, self.current)
							a.h = self.getHCost(a, self.goal)
							self.OPENList.append(a)
					else:
						travelCost = self.current.g + self.getGCost(self.current, a)
						if (travelCost < a.g):
							a.parent = self.current
							a.setG(self.getGCost(self.current, a))
							a.setH(self.getHCost(self.goal, a))
							self.OPENList.sort(key = lambda x : x.f)
		return False
		
	def locateAdjacent(self): #function that finds current node adjacents
		ADJACENTList = self.ADJACENTList
		for a,nodes in enumerate(self.searchSpace): #get current node
			for b,node in enumerate(nodes):
				if node == self.current:
					position = (b, a)
		for a,nodes in enumerate(self.searchSpace): #get adjacent nodes
			if (position[1] - 1 <= a <= position[1] + 1): 
				for b,node in enumerate(nodes):
					if (position[0] - 1 <= b <= position[0] + 1) and (self.searchSpace[a][b].walkable == True) and (self.searchSpace[a][b] != self.current):
						ADJACENTList.append(self.searchSpace[a][b])
		return ADJACENTList
		
	def lowestFCost(self, nodes): #lowest f cost function. used to fine lowest f
		lowestF = self.lowestF
		for n in nodes: #for setting lowestF. if its none or greater than n, it becomes n
			if (lowestF == None) or (n.getF() < lowestF.getF()):
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
		distanceA = abs(row[0] - column[0]) #obtain absolute value
		distanceB = abs(row[1] - column[1]) #obtain absolute value
		hCost = (distanceA * 10) + (distanceB * 10) #multiply both distances by ten and add them
		return hCost #return cost
		
	def getGCost(self, node1, node2): #calculates g
		gCost = self.gCost
		for a,nodes in enumerate(self.searchSpace): #these for loops get the current node
			for b,node in enumerate(nodes):
				if (self.searchSpace[a][b] == node1): #rows
					row = [a,b]
				if (self.searchSpace[a][b] == node2): #columns
					column = [a,b]
		distanceA = abs(row[0] - column[0]) #obtain absolute value
		distanceB = abs(row[1] - column[1]) #obtain absolute value
		A = distanceA * distanceA #multiply disA with disA
		B = distanceB * distanceB #multiply disB with disB
		C = A + B #add A and B
		gCost = (sqrt(C) * 10) #square root C and multiply it by ten
		return gCost #return cost
		
	def drawPath(self, screen): #draws the path from goal to start
		temp = self.goal #temp variable uses goal value
		cPath = self.pathColor #purple color value
		while (temp.parent != None): #when parent isn't none...draw line
			pygame.draw.line(screen, cPath, temp.center, temp.parent.center, 5)
			temp = temp.parent #temp now equals parent value
			
	def drawCircle(self, screen): #draws circles on the path from goal to start
		temp = self.goal #temp variable uses goal value
		cPath = self.pathColor #purple color value
		while (temp.parent != None): #when parent isn't none...draw circle
			pygame.draw.circle(screen, cPath, temp.parent.center, 5, 5)
			temp = temp.parent #temp now equals parent value
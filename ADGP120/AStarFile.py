import pygame, NodesFile, math #using pygame, NodesFile and math
from pygame import * #import everything
from NodesFile import * #import everything
from math import * #import everything

class AStar(object): #astar class. used to create astar objects
	def __init__(self, start, searchSpace, goal): #init function. used to setup variables
		self.OPENList = [] #holds nodes that need to be calculated
		self.CLOSEList = [] #when calculations are done, add to this list
		self.ADJACENTList = [] #nodes that surround the current node
		self.start = start #start node
		self.current = start #starts as start node
		self.goal = goal #end node
		self.searchSpace = searchSpace #search range
		self.startColor = (255,255,0) #yellow color value
		self.goalColor = (0,255,0) #green color value
		self.pathColor = (255,105,180) #pink color value
		self.lowestF = None #holds lowest f
		self.hCost = 0 #holds h cost
		self.gCost = 0 #holds g cost
		
	def draw(self, screen): #draws start node and goal node
		cStart = self.startColor #yellow color value
		pygame.draw.rect(screen, cStart, (self.start.x, self.start.y, self.start.width, self.start.height)) #draws start node
		cGoal = self.goalColor #green color value
		pygame.draw.rect(screen, cGoal, (self.goal.x, self.goal.y, self.goal.width, self.goal.height)) #draws goal node
			
	def run(self): #run function. This "runs" the astar algorithm
		self.current = self.start #current is start
		self.OPENList.append(self.current) #add current to open list
		adjacent = self.locateAdjacent() #find the adjacents
		for a in adjacent: #for everything in adjacent...
			if (a.walkable == True): #if true...do this
				a.parent = self.current #"a"s parent equals current
				a.g = self.getGCost(a, self.current) #g has new cost value
				a.h = self.getHCost(a, self.goal) #h has new cost value
				self.OPENList.append(a) #add a to open list
		self.OPENList.remove(self.current) #remove current from open
		self.CLOSEList.append(self.current) #add current to closed
		while (len(self.OPENList)): #while open list has data...
			self.current = self.lowestFCost(self.OPENList) #find the lowest f node in the open list and apply it to current
			self.OPENList.remove(self.current) #remove current from open
			self.CLOSEList.append(self.current) #add current to closed
			adjacentNode = self.locateAdjacent() #find the adjacents
			if (self.goal in self.CLOSEList) or (self.current == self.goal): #if the goal node is in the closed list or if current node is equal to the goal node...
							return True #stop and return true
			for a in adjacentNode: #for everything in adjacentNode...
				if (a not in self.CLOSEList): #if a is not included in the close list...move on to next check
					if (a not in self.OPENList): #if a is not included in the open list...move on to next check
						a.parent = self.current #"a"s parent equals current
						a.g = self.getGCost(a, self.current) #g has new cost value
						a.h = self.getHCost(a, self.goal) #h has new cost value
						self.OPENList.append(a) #add a to open list
					else: #otherwise...
						costToMove = self.current.g + self.getGCost(a, self.current) #this variable holds the sum of currents g cost and the value from getGCost
						if (costToMove < a.g): #if costToMove value is last than a's current g cost...
							a.parent = self.current #"a"s parent equals current
							a.g = self.getGCost(a, self.current) #g has new cost value
							self.OPENList.sort() #sort the open list
		return False #if not true, return false
		
	def locateAdjacent(self): #function that finds current node adjacents
		ADJACENTList = self.ADJACENTList #variable equals list
		for a,nodes in enumerate(self.searchSpace): #get current node
			for b,node in enumerate(nodes): #enumerate returns a iterator (or sequence). [(a, node[0]),(a, node[1])...]
				if (node == self.current): #if node equals current...
					position = (a, b) #create position variable
		for a,nodes in enumerate(self.searchSpace): #get adjacent nodes
			if (position[0] - 1 <= a <= position[0] + 1): #if a is greater or equal to positions first index - 1, less or equal to positions first index + 1...move on and do the same for b
				for b,node in enumerate(nodes): #enumerate returns a iterator (or sequence). [(a, node[0]),(a, node[1])...]
					if (position[1] - 1 <= b <= position[1] + 1): #if b is greater or equal to positions second index - 1, less or equal to positions second index + 1...move on
						if (self.searchSpace[a][b].walkable == True) and (self.searchSpace[a][b] != self.current): #if searchSpace list is walkable and is not the current node...
							ADJACENTList.append(self.searchSpace[a][b]) #add the searchSpace list to the adjacent list
		return ADJACENTList #return list
		
	def lowestFCost(self, nodes): #lowest f cost function. used to fine lowest f
		lowestF = self.lowestF #variable equals value
		for n in nodes: #for setting lowestF. if its none or greater than n, it becomes n
			if (lowestF == None) or (n.getF() < lowestF.getF()):
				lowestF = n
		return lowestF #return new value
		
	def getHCost(self, pos1, pos2): #calculates h
		hCost = self.hCost #variable equals value
		for a,nodes in enumerate(self.searchSpace): #these for loops get the current node
			for b,node in enumerate(nodes): #these for loops get the current node
				if (self.searchSpace[a][b] == pos1): #if searchSpace is equal to the first position...
					row = [a,b] #rows
				if (self.searchSpace[a][b] == pos2): #if searchSpace is equal to the second position...
					column = [a,b] #columns
		distanceA = abs(row[0] - column[0]) #obtain absolute value of first distance
		distanceB = abs(row[1] - column[1]) #obtain absolute value of second distance
		hCost = 10 * (distanceA + distanceB) #add both distances and multiply by ten
		return hCost #return cost
		
	def getGCost(self, pos1, pos2): #calculates g
		gCost = self.gCost #variable equals value
		for a,nodes in enumerate(self.searchSpace): #these for loops get the current node
			for b,node in enumerate(nodes): #these for loops get the current node
				if (self.searchSpace[a][b] == pos1): #if searchSpace is equal to the first position...
					row = [a,b] #rows
				if (self.searchSpace[a][b] == pos2): #if searchSpace is equal to the second position...
					column = [a,b] #columns
		distanceA = abs(row[0] - column[0]) #obtain absolute value of first distance
		distanceB = abs(row[1] - column[1]) #obtain absolute value of second distance
		A = distanceA * distanceA #multiply disA with itself
		B = distanceB * distanceB #multiply disB with itself
		C = A + B #add A and B then set value to variable
		gCost = (sqrt(C) * 10) #square root C and multiply it by ten
		return gCost #return cost
		
	def drawPath(self, screen): #draws the path from goal to start
		temp = self.goal #temp variable uses goal value
		cPath = self.pathColor #pink color value
		while (temp.parent != None): #when parent isn't none...draw line
			pygame.draw.line(screen, cPath, temp.center, temp.parent.center, 5) #draws path to goal node. this is the shortest path line
			temp = temp.parent #change temps value
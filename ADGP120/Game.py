import pygame, NodesFile, AStarFile, random #using pygame, NodesFile, AStarFile and random
from pygame import * #import everything
from NodesFile import * #import everything
from AStarFile import * #import everything
from random import * #import everything

def main(): #main function. 
	pygame.init() #init pygame
	window = [627,505] #set window size
	screen = pygame.display.set_mode(window) #setup screen to display window variable
	pygame.display.set_caption("ADGP120 Script It Up - AStar") #name on window
	searchSpace = [] #searchSpace list
	tracker = 0 #used for tracking the nodes height position
	n = Node(0, 0) #node object
	colorTeal = (0,255,255) #teal color value
	colorBlue = (0,0,255) #blue color value
	colorBrown = (139,69,19) #brown color value
	
	for a in range(0, 20): #this range determines how many rows for the grid
		randStart = randrange(0, 20) #determines where the start node will spawn
		randGoal = randrange(0, 20) #determines where the goal node will spawn
		temp = [] #temp list, holds new node object
		for b in range(0, 25): #this range determines how many columns for the grid
			temp.append(Node(b * (n.width + n.margin), tracker)) #add new node object to list
		searchSpace.append(temp) #add temp to searchSpace list
		tracker += temp[0].height + temp[0].margin #the temp index height + margin value and adds it to the tracker variable
	program = AStar(searchSpace[randStart][randStart], searchSpace, searchSpace[randGoal][randGoal]) #AStar object. takes start node first, then searchSpace list, then goal node
	                             
	for a in searchSpace: #used to randomize walkable paths
		for b in a: #used to randomize walkable paths
			randGrid = randrange(0, 5) #range the random values use
			if (randGrid % 3 == 0): #if the value mod 3 equal to zero...move to next step
				if (program.goal != b) and (program.start != b): #if goal and start do not equal b...
					b.walkable = False #walkable is false
			b.draw(screen) #generates grid
			
	program.draw(screen) #calls draw function
	program.run() #calls run function
	
	for o in program.OPENList: #for everything in the open list...
			if o != program.goal: #if the node in the open list is not the goal node...
				pygame.draw.rect(screen, colorBlue, (o.x, o.y, o.width, o.height)) #draw this (blocks will be colored dark blue)		
	for c in program.CLOSEList: #for everything in the closed list...
			if (c != program.start) and (c != program.goal): #if the node in the closed list is not the start node and is not the goal node...
				pygame.draw.rect(screen, colorTeal, (c.x, c.y, c.width, c.height)) #draw this (blocks will be colored light blue)				
	for s in program.searchSpace: #for everything in the searchSpace list...
		for p in s: #for everything in s...
			if p.parent != None: #if the parent node has a value...
				pygame.draw.line(screen, colorBrown, p.center, p.parent.center, 5) #draw these (blocks will have a brown line and circle in them)
				pygame.draw.circle(screen, colorBrown, p.center, 5, 0)
	
	program.drawPath(screen) #this will draw a pink line. this will show the shortest possible path to the goal node.
	
	finished = False #set finished variable to false
	while not finished: #while finished is still false...
		for event in pygame.event.get(): #searchs for the end event. Once found, return true
			if event.type == pygame.QUIT:
				finished = True	
		pygame.display.flip()
	pygame.quit()
main()
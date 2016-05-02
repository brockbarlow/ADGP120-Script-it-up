import pygame, NodesFile, AStarFile, random #using pygame, NodesFile, AStarFile and random
from pygame import * #import everything
from NodesFile import * #import everything
from AStarFile import * #import everything
from random import * #import everything

def main(): #main function. 
	pygame.init() #init pygame
	window = [997,797] #set window size
	screen = pygame.display.set_mode(window) #setup screen to display window variable
	pygame.display.set_caption("ADGP120 Script It Up - AStar") #name on window
	searchSpace = [] #searchSpace list
	tracker = 0 #used for tracking the nodes height position
	n = Node(0, 0) #node object
	colorTeal = (0,255,255) #teal color value
	colorBlue = (0,0,255) #blue color value
	colorPink = (255,105,180) #pink color value
	
	for a in range(0, 32): #this range determines how many rows for the grid
		randStart = randrange(0, 32) #determines where the start node will spawn
		randGoal = randrange(0, 32) #determines where the goal node will spawn
		temp = [] #temp list, holds new node object
		for b in range(0, 55): #this range determines how many columns for the grid
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
			
	program.draw(screen) 
	program.run()
	
	for o in program.OPENList:
			if o != program.goal:
				pygame.draw.rect(screen, colorBlue, (o.x, o.y, o.width, o.height))
				
	for c in program.CLOSEList:
			if (c != program.start) and (c != program.goal):
				pygame.draw.rect(screen, colorTeal, (c.x, c.y, c.width, c.height))
				
	for s in program.searchSpace:
		for p in s:
			if p.parent != None:
				pygame.draw.line(screen, colorPink, p.center, p.parent.center, 5)
				pygame.draw.circle(screen, colorPink, p.center, 5, 0)
	
	program.drawPath(screen)
	
	finished = False
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True	
		pygame.display.flip()
	pygame.quit()
main()
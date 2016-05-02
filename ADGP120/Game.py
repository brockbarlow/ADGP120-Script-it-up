import pygame, NodesFile, AStarFile, random #using pygame, NodesFile, AStarFile and random
from pygame import * #import everything
from NodesFile import * #import everything
from AStarFile import * #import everything
from random import * #import everything

def main(): #main function. 
	pygame.init() #init pygame
	window = [997,797] #set window size
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("ADGP120 Script It Up - AStar") #name on window
	searchSpace = [] #array variable
	tracker = 0 #used for tracking
	n = Node(0, 0) #node object
	colorTeal = (0,255,255)
	colorBlue = (0,0,255)
	colorPink = (255,105,180)
	
	for a in range(0, 32):
		randStart = randrange(0, 32)
		randGoal = randrange(0, 32)
		temp = [] #holds new node object
		for b in range(0, 55):
			temp.append(Node(b * (n.width + n.margin), tracker)) #add new node object to array
		searchSpace.append(temp)
		tracker += temp[0].height + temp[0].margin
	program = AStar(searchSpace[randStart][randStart], searchSpace, searchSpace[randGoal][randGoal]) #AStar object
	                             
	for a in searchSpace: #used to randomize walkable paths
		for b in a:
			randGrid = randrange(0, 5)
			if (randGrid % 3 == 0):
				if (program.goal != b) and (program.start != b):
					b.walkable = False
			b.draw(screen)
			
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
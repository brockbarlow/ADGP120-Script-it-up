import pygame, NodesFile, AStarFile, random, time #using pygame, NodesFile, AStarFile, random and time
from pygame import * #import everything
from NodesFile import * #import everything
from AStarFile import * #import everything
from random import * #import everything
from time import * #import everything

def main():
	pygame.init()
	window = [622,472]
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("AStar")
	searchSpace = []
	temp = []
	trackNode = 0
	n = Node(-10, -10)
	
	for a in range(0, 19):
		randStart = randrange(0, 19)
		randGoal = randrange(0, 19)
		temp = []
		for b in range(0, 25):
			temp.append(Node(b * (n.width + n.margin), trackNode))
		searchSpace.append(temp)
		trackNode += temp[0].height + temp[0].margin
	program = AStar(searchSpace[randStart][randStart], searchSpace, searchSpace[randGoal][randGoal])
	                               #y         #x                                   #y        #x
	for a in searchSpace:
		for b in a:
			randGrid = randrange(0, 5)
			if (randGrid % 3 == 0) and (program.goal != b) and (program.start != b):
				b.walkable = False
			b.draw(screen)
			
	program.draw(screen)
	program.run()#screen)
	program.drawPath(screen)
	program.drawCircle(screen)
	
	finished = False
	clock = pygame.time.Clock()
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True	
		clock.tick(60)
		pygame.display.flip()
	pygame.quit()
	
main()
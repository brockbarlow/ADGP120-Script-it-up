import pygame, NodesFile, AStarFile, random #using pygame, NodesFile, AStarFile and random
from pygame import * #import everything
from NodesFile import * #import everything
from AStarFile import * #import everything
from random import * #import everything

def main():
	pygame.init()
	window = [622,472]
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("ADGP120 Script It Up - AStar")
	searchSpace = []
	temp = []
	trackNode = 0
	n = Node(0, 0)
	
	for a in range(0, 19):
		randStart = randrange(0, 19)
		randGoal = randrange(0, 19)
		temp = []
		for b in range(0, 25):
			temp.append(Node(b * (n.width + n.margin), trackNode))
		searchSpace.append(temp)
		trackNode += temp[0].height + temp[0].margin
	program = AStar(searchSpace[randStart][randStart], searchSpace, searchSpace[randGoal][randGoal])
	                             
	for a in searchSpace:
		for b in a:
			randGrid = randrange(0, 5)
			if (randGrid % 3 == 0):
				if (program.goal != b) and (program.start != b):
					b.walkable = False
			b.draw(screen)
			
	program.draw(screen)
	program.run()
	program.drawPath(screen)
	program.drawCircle(screen)
	
	finished = False
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True	
		pygame.display.flip()
	pygame.quit()
	
main()
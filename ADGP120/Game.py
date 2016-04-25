import pygame, NodesFile, AStarFile, random, time
from pygame import *
from NodesFile import *
from AStarFile import *
from random import *
from time import *

def main():
	pygame.init()
	window = [247,247]
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("AStar")
	searchSpace = []
	temp = []
	trackNode = 0
	n = Node(-10, -10)
	
	for a in range(0, 10):
		temp = []
		for b in range(0, 10):
			temp.append(Node(b * (n.width + n.margin), trackNode))
		searchSpace.append(temp)
		trackNode += temp[0].height + temp[0].margin
	program = AStar(searchSpace[2][2], searchSpace, searchSpace[7][7])
	
	for a in searchSpace:
		for b in a:
			randGrid = randrange(0, 10)
			if (randGrid % 3 == 0) and (program.goal != b) and (program.start != b):
				b.walkable = False
			b.draw(screen)
			
	program.draw(screen)
	program.run(screen)
	program.drawPath(screen)
	
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
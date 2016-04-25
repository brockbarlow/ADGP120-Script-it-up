import pygame, NodesFile, AStarFile, random, time
from pygame import *
from NodesFile import *
from AStarFile import *
from random import *
from time import *

def main():
	pygame.init()
	window = [250,250]
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("ADGP120")
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
	program = AStar(searchSpace[1][1], searchSpace, searchSpace[5][5])
	
	for a in searchSpace:
		for b in a:
			b.draw(screen)
			
	program.draw(screen)
	program.run(screen)
	
	#for x in range(10):
		#for y in range(10):
			#n = Node(x,y)
			#unwalkable = True if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.position))
			#n.setWalk(unwalkable)
			#searchSpace.append(n)
	
	finished = False
	clock = pygame.time.Clock()
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True	
		#screen.fill(0,0,0)
		clock.tick(60)
		#for i in searchSpace:
			#i.draw(screen)
		pygame.display.flip()
	pygame.quit()
	
main()
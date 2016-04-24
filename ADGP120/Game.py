import pygame, NodesFile, AStar, random, time
from pygame import *
from NodesFile import *
from AStar import *
from random import *
from time import *

def main():
	pygame.init()
	window = [640,480]
	screen = pygame.display.set_mode(window)
	pygame.display.set_caption("ADGP120")
	
	searchSpace = []
	for x in range(10):
		for y in range(10):
			n = Node(x,y)
			unwalkable = True if (x >= 5 and x <= 6 and y >= 5 and y <= 8) else False
			print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.position))
			n.setWalk(unwalkable)
			searchSpace.append(n)
	
	finished = False
	clock = gfx.time.Clock()
	while not finished:
		for event in gfx.event.get():
			if event.type == gfx.QUIT:
				finished = True	
		screen.fill(0,0,0)
		clock.tick(60)
		for i in searchSpace:
			i.draw(screen)
		pygame.display.flip()
	pygame.quit()
	
main()
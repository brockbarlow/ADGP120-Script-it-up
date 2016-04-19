import testArray
from testArray import *
import pygame
from pygame.locals import *

class Sort:
	def __init__(self):
		self.open([])
		self.close([])
		
	def lowest(self, arrays):
		lowest = -1
		THElowest = None
		for i in arrays:
			if (i < lowest):
				lowest = i
				THElowest = lowest
		return THElowest
			
def main():
	array.sort()

main()
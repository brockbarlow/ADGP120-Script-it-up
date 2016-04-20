class TestArray(object):
	def __init__(self, array, start):
		self.f = None
		self.array = ([5,3,9,7,1,2,4,8])
		self.open([])
		self.close([])
		
	def getF(self):
		return self.array
		
	def run(self):
		self.open.append(start)
		while not self.open:
			current = self.lowestF(self.open)
		
	def lowestF(self, array):
		lowestF = -1
		lowestInArray = None
		for i in array:
			if (i.f < lowestF):
				lowestF = i.f
				lowestInArray = i
		
		return lowestInArray
		
'''
class Sort(object):
	def __init__(self):
		self.open([])
		self.close([])
		
	def lowest(self, array):
		lowest = -1
		THElowest = None
		for i in array:
			if (i < lowest):
				lowest = i
				THElowest = lowest
		return THElowest
		
def main():
	#TestArray.x.sort()
	#TestArray.y.sort()
main()
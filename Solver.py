from State import *
from Solution import *
from collections import defaultdict

class Solver:
	
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		self.start = start
		self.end = end
		self.graph = graph
		self.solution = None		
		return
			
	def read(self, file):
		f = open(file, "r")
		
		while True:
			line = f.readline()
			if not line: break
		
			res = list(map(float, line.split()))
			#						from state									to state				  cost
			self.graph[State(float(res[0]), float(res[1]))].append([State(float(res[2]), float(res[3])), res[4]])
			#					    x				y							 x1				y1			-
		return self.graph
	
	def setSolution(self, end, iterations, branchingSum, expandedNodes, visited, time_elapsed):
		itr = self.end
		path = []
		c = 0
		
		while True:
			if itr:
				path.append(itr)
				itr = itr.getFather()
			else:
				path.reverse()
				
				if(len(path) == 1 and end == path[0]):
					path.pop()
				cost = 0
				for j in range(0, len(path)-1):
					for i in range(0, len(self.graph[path[j]])):
						if self.graph[path[j]][i][0] == path[j + 1]:
							cost = cost + self.graph[path[j]][i][1]	
				
				if iterations == 0:
					branchFactor = 0
				else:
					branchFactor = branchingSum/iterations
				
				self.solution = Solution(path, cost, expandedNodes, branchFactor, len(visited), time_elapsed, iterations)
				break	
				
		return self.solution		
	
	

import time
from Solver import *
from Solution import *
try:
	import Queue as Q
except ImportError:
	import queue as Q


class GreedySearch(Solver):
	def __init__(self, start = State(), end = State(), graph = defaultdict(list)):
		super(GreedySearch, self).__init__(start, end, graph)
		self.heap = Q.PriorityQueue()
	
	def heuristic(self, stateA, stateB):
		posA = stateA.getPos()
		posB = stateB.getPos()
		
		return math.sqrt((posB[0] - posA[0]) + (posB[1] - posA[1]))
	
	def solve():
		expandedNodes = 0
		branchingSum = 0
		iterations = 0
		start_time = time.time()
		self.start.setPriority(0)
		self.heap.put(self.start)
		visited = [self.start]
		
		while not self.heap.empty():
			state = self.heap.get()
			
			if state == self.end:
				self.end = state
				break
			
			expandedNodes = expandedNodes + 1
			iterations = iterations + 1
			
			for s in self.graph[state]: 
				if s[0] not in visited:
					depth = s[0].getDepth() + 1
					branchingSum = branchingSum + 1
					h = heuristic(state, s)
					
					s[0].setDepth(depth)
					s[0].setFather(state)
					s[0].increaseCostSoFar(s[1])
					s[0].setPriority(h)	
					
					self.heap.put(s[0])
					visited.append(s[0])
		
		end_time = time.time()
		
		itr = self.end
		cost = itr.getCost()
		path = []
		time_elapsed = end_time - start_time
		
		while True:
			if itr:
				path.append(itr)
				itr = itr.getFather()
			else:
				path.reverse()
				if iterations == 0:
					branchFactor = 0
				else:
					branchFactor = branchingSum/iterations
				self.solution = Solution(path, cost, expandedNodes, branchFactor, len(visited), time_elapsed)
				break
		
		return self.solution


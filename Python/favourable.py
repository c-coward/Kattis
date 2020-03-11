from sys import stdin
from collections import deque

def main():
	t = int(stdin.readline())

	for _ in range(t):
		s = int(stdin.readline())
		leaves = deque() # Hold favorable endings with paths
		parents = {} # Holds parents of children
		scores = {1:1} # Number of paths that go through a node
		# When 1 is reached, a new path has been found

		for _ in range(s):
			line = stdin.readline().split()

			node = int(line[0])

			if len(line) == 4: # Node is a parent
				childr = set(map(int,line[1:]))

				for ch in childr: # Add node as parent of all children
					if ch not in parents: parents[ch] = set()
					parents[ch].add(node)

			else: # Node is a leaf
				word = line[1]
				if word == 'favourably': # Node is part of a path
					leaves.append((node,-1))

		count = 0
		path = {} # Path of most previously visited nodes
		# Perform a DFS starting from each leaf until a scored node is found
		while leaves:
			leaf,prev = leaves.pop()
			path[leaf] = prev
		
			if leaf in scores: # Node has already been visited, is known to be on a path
				count += scores[leaf]

				# Iterate through the path taken, updating scores along the way
				p = prev
				while p != -1:
					if p not in scores: scores[p] = 0
					scores[p] += scores[leaf]
					p = path[p]

			else:
				for par in parents[leaf]:
					leaves.append((par,leaf)) # Move on to the next node in the path

		print(count)

main()
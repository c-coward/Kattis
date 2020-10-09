from collections import deque

def main():
	n, h, l = map(int, input().split())
	horribleness = [float('inf') for _ in range(n)]
	horrors = list(map(int, input().split()))
	
	# Graph of neighbors
	graph = {num: set() for num in range(n)}
	for _ in range(l):
		a, b = map(int, input().split())
		graph[a].add(b)
		graph[b].add(a)

	# Perform a BFS on all the movies
	q = deque()
	for horror in horrors:
		q.append((horror, 0))
	
	while q:
		# Index of movie, and its minimal horror index
		i, h = q.popleft()
		# If horribleness has been set, then h is not the minimal value
		if horribleness[i] != float('inf'): continue

		# Update the horribleness of the movie
		horribleness[i] = h

		# Update the neighbors of this movie
		for j in graph[i]:
			if horribleness[j] != float('inf'): continue
			# Since j is one movie away from i, it is slightly less horrible
			q.append((j, h + 1))

	max_hi = 0
	for i in range(n):
		if horribleness[i] > horribleness[max_hi]:
			max_hi = i

	print(max_hi)

if __name__ == "__main__":
	main()
def main():
	to_find = "ICPCASIASG" # String to spell out on chessboard
	dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
	
	# Take inputs
	n = int(input())
	line = input()
	# Create structures used in search
	graph = []
	q = []
	
	# Construct graph and find starting points ("I"s)
	for i in range(n):
		graph.append(line[n*i:n*i+n])
		for j in range(n):
			if graph[i][j] == 'I':
				q.append((i,j,0))

	found = False
	# Perform a DFS from each starting position
	while q:
		y,x,curr = q.pop()

		# Check if at the end of the string
		if curr == 9:
			found = True
			break

		for i,j in dirs:
			# Make sure new point is in bounds and the letter im looking for
			if 0 <= y+i < n and 0 <= x+j < n:
				if graph[y+i][x+j] == to_find[curr+1]:
					q.append((y+i,x+j,curr+1))

	print("YES" if found else "NO")

main()
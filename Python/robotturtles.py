from heapq import heappop as pop, heappush as push

def main():
	graph = [list(input()) for _ in range(8)]
	visited = [[False for _ in range(8)] for _ in range(8)]
	
	ti,tj = 7,0
	graph[ti][tj] = '.'

	q = []
	push(q,(0,ti,tj,0,[]))

	# 0,1,2,3 = R,D,L,U
	dirs = [(0,1,0),(1,0,1),(0,-1,2),(-1,0,3)] 

	while q:
		m,i,j,f,p = pop(q) # Moves,Y,X,Facing,Path
		if graph[i][j] == 'D':
			break

		if visited[i][j]: continue
		visited[i][j] = True

		for di,dj,df in dirs:
			if (0 <= i+di < 8 and 0 <= j+dj < 8
					and not visited[i+di][j+dj]):
				new_path = []
				
				if graph[i+di][j+dj] == 'C':
					continue

				if df != f:
					if abs(df-f) == 2:
						new_path.append('R')
						new_path.append('R')
					elif df == f+1:
						new_path.append('R')
					elif df == f-1:
						new_path.append('L')
					elif df == f+3:
						new_path.append('L')
					else:
						new_path.append('R')

				if graph[i+di][j+dj] == 'I':
					new_path.append('X')

				new_path.append('F')
				push(q,(m+len(new_path),i+di,j+dj,df,p+new_path))

	if graph[i][j] == 'D':
		print(''.join(p))
	else:
		print('no solution')

main()
from sys import stdin

def main():
	# Find corners of coordinate system
	ymin,ymax = 0,0
	xmin,xmax = 0,0

	cx,cy = 0,0
	visited = set()
	for line in stdin:
		line = line.strip()
		if line == 'down':
			cy -= 1
		elif line == 'up':
			cy += 1
		elif line == 'left':
			cx -= 1
		elif line == 'right':
			cx += 1

		ymin = min(ymin,cy)
		ymax = max(ymax,cy)

		xmin = min(xmin,cx)
		xmax = max(xmax,cx)

		# Keep track of spots on path
		visited.add((cx,cy))

	sx,sy = 0,0
	shift_x, shift_y = 0, 0

	# Shift coordinates to normalize bottom left as (0,0)
	if xmin != 0:
		shift_x = -xmin
	if ymin != 0:
		shift_y = -ymin

	# Add 1 to include the endpoints on the coordinate system
	# Add 2 for the buffer
	graph = [[' ' for _ in range(xmax+shift_x+1+2)] for _ in range(ymax+shift_y+1+2)]


	# Add 1 when plotting any point to account for the buffer
	for x,y in visited:
		graph[y+shift_y+1][x+shift_x+1] = '*'
	graph[sy+shift_y+1][sx+shift_x+1] = 'S'
	graph[cy+shift_y+1][cx+shift_x+1] = 'E'

	# Apply the buffer
	for j in range(len(graph[0])):
		graph[0][j] = '#'
		graph[-1][j] = '#'
	for i in range(len(graph)):
		graph[i][0] = '#'
		graph[i][-1] = '#'

	# Since increasing y moves down the grid, flip board and print
	for g in graph[::-1]: print(''.join(g))

main()
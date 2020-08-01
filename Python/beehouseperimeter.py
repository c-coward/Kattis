from collections import deque

def main():
	r, k = map(int, input().split())
	# First, generate the hive and set all cells to empty (0)
	borderless_hive = [0 for _ in range(3 * r * r - 3 * r + 1)]
	# Set all house cells to full (1)
	for cell in map(int, input().split()):
		borderless_hive[cell - 1] = 1

	# Generate the lengths of each row in the hive
	borderless_lengths = [r + i for i in range(r)] + [r + i for i in range(r - 2, -1, -1)]
	
	# Create a hive with a border of empty cells
	hive = [0 for _ in range(r + 2)]
	start = 0
	for l in borderless_lengths:
		hive += borderless_hive[start : start + l] + [0, 0]
		start += l
	hive += [0 for _ in range(r)]

	r += 1
	# Generate the lengths of each row in the new hive
	lengths = [r + i for i in range(r)] + [r + i for i in range(r - 2, -1 ,-1)]

	# Generate the bounds of each row in the new hive
	bounds = [0]
	for l in lengths:
		bounds.append(bounds[-1] + l)

	# Finally, perform a BFS on the hive to find all edges of house cells
	visited = [0 for _ in range(len(hive))]
	q = deque([(0, 0)]) # Deque of tuples (index, row)
	visited[0] = 1
	perimeter = 0

	# Very messy BFS, many statements could be refactored, but it gets the job done
	while q:
		index, row = q.popleft()

		# If this is a house cell, increase perimeter but dont update neighbors
		if hive[index]:
			perimeter += 1
			continue
		
		# Check the 2 adjacent cells in the same row as this cell

		if index - 1 >= bounds[row] and not visited[index - 1]:
			q.append((index - 1, row))
			if not hive[index - 1]:
				visited[index - 1] = 1

		if index + 1 < bounds[row + 1] and not visited[index + 1]:
			q.append((index + 1, row))
			if not hive[index + 1]:
				visited[index + 1] = 1

		if row < r - 1:
			# Check the 2 cells above this cell
			if row > 0:
				if index - lengths[row] >= bounds[row - 1] and not visited[index - lengths[row]]:
					q.append((index - lengths[row], row - 1))
					if not hive[index - lengths[row]]:
						visited[index - lengths[row]] = 1

				if index - lengths[row] + 1 < bounds[row] and not visited[index - lengths[row] + 1]:
					q.append((index - lengths[row] + 1, row - 1))
					if not hive[index - lengths[row] + 1]:
						visited[index - lengths[row] + 1] = 1

			# Check the 2 cells below this cell, which must exist

			if not visited[index + lengths[row]]:
				q.append((index + lengths[row], row + 1))
				if not hive[index + lengths[row]]:
					visited[index + lengths[row]] = 1

			if not visited[index + lengths[row] + 1]:
				q.append((index + lengths[row] + 1, row + 1))
				if not hive[index + lengths[row] + 1]:
					visited[index + lengths[row] + 1] = 1

		elif row > r - 1:
			# Check the 2 cells above this cell, which must exist

			if not visited[index - lengths[row]]:
				q.append((index - lengths[row], row - 1))
				if not hive[index - lengths[row]]:
					visited[index - lengths[row]] = 1

			if not visited[index - lengths[row] - 1]:
				q.append((index - lengths[row] - 1, row - 1))
				if not hive[index - lengths[row] - 1]:
					visited[index - lengths[row] - 1] = 1

			# Check the 2 cells below this cell
			if row < 2 * r - 2:
				if index + lengths[row] < bounds[row + 2] and not visited[index + lengths[row]]:
					q.append((index + lengths[row], row + 1))
					if not hive[index + lengths[row]]:
						visited[index + lengths[row]] = 1

				if index + lengths[row] - 1 >= bounds[row + 1] and not visited[index + lengths[row] - 1]:
					q.append((index + lengths[row] - 1, row + 1))
					if not hive[index + lengths[row] - 1]:
						visited[index + lengths[row] - 1] = 1
		
		else:
			# Check the 2 cells above this cell

			if index - lengths[row] >= bounds[row - 1] and not visited[index - lengths[row]]:
				q.append((index - lengths[row], row - 1))
				if not hive[index - lengths[row]]:
					visited[index - lengths[row]] = 1

			if index - lengths[row] + 1 < bounds[row] and not visited[index - lengths[row] + 1]:
				q.append((index - lengths[row] + 1, row - 1))
				if not hive[index - lengths[row] + 1]:
					visited[index - lengths[row] + 1] = 1

			# Check the 2 cells below this cell

			if index + lengths[row] < bounds[row + 2] and not visited[index + lengths[row]]:
				q.append((index + lengths[row], row + 1))
				if not hive[index + lengths[row]]:
					visited[index + lengths[row]] = 1

			if index + lengths[row] - 1 >= bounds[row + 1] and not visited[index + lengths[row] - 1]:
				q.append((index + lengths[row] - 1, row + 1))
				if not hive[index + lengths[row] - 1]:
					visited[index + lengths[row] - 1] = 1

	print(perimeter)

if __name__ == '__main__':
	main()
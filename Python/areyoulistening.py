import math

def main():
	cx, cy, n = map(int, input().split())
	distances = []

	for _ in range(n):
		x, y, r = map(int, input().split())

		distance_to_center = math.hypot(cx - x, cy - y)

		if distance_to_center <= r:
			distance_to_center = r

		distances.append(distance_to_center - r)

	distances.sort()
	print(math.floor(distances[2]))

main()
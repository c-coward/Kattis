from sys import stdin

def main():
	radii = [20**2,40**2,60**2,80**2,100**2,120**2,140**2,160**2,180**2,200**2]
	t = int(stdin.readline())
	outs = []

	for _ in range(t):
		n = int(stdin.readline())
		points = 0
		for _ in range(n):
			x,y = map(int,stdin.readline().split())
			dist = x**2 + y**2

			for i in range(10):
				if dist <= radii[i]:
					points += 10-i
					break
					
		outs.append(str(points))
	print('\n'.join(outs))

main()
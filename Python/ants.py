from sys import stdin
def main():
	t = int(stdin.readline())
	outs = []
	for _ in range(t):
		l,n = map(int,stdin.readline().split())

		tot = 0
		left = []
		right = []
		while tot < n:
			ants = map(int,stdin.readline().strip().split())
			for a in ants:
				tot += 1
				if a <= l//2:
					left.append(a)
				else:
					right.append(a)

		left.sort()
		right.sort()

		lower,upper = -1,-1
		if not left:
			lower = l-right[0]
			upper = right[-1]
		elif not right:
			lower = left[-1]
			upper = l-left[0]
		else:
			upper = max(l-left[0],right[-1])
			lower = max(left[-1],l-right[0])

		outs.append('%d %d' % (lower,upper))
	for o in outs: print(o)

main()
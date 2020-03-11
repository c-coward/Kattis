from math import inf

def main():
	n = int(input())

	platforms = [(0,-inf,inf)]
	for _ in range(n):
		h,s,e = map(int,input().split())
		platforms.append((h,s,e))

	platforms = sorted(platforms,reverse=True)

	heights = 0
	for i in range(n):
		right = False
		left = False

		h,s,e = platforms[i]

		for j in range(i+1,n+1):
			h2,s2,e2 = platforms[j]
			if not left:
				if s2 <= s < e2:
					left = True
					heights += h-h2

			if not right:
				if s2 < e <= e2:
					right = True
					heights += h-h2

	print(heights)

if __name__ == '__main__': main()
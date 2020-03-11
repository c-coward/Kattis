from sys import stdin
def main():
	n,m = map(int,stdin.readline().split())
	fish = list(map(int,stdin.readline().split()))
	fishmongers = []
	for _ in range(m):
		x,p = map(int,stdin.readline().split())
		fishmongers.append((p,x))

	fish = sorted(fish,reverse=True)
	fishmongers = sorted(fishmongers,reverse=True)

	monies = 0
	i = 0
	for p,x in fishmongers:
		for _ in range(x):
			monies += fish[i]*p
			i += 1
			if i == n: break
		if i == n: break

	print(monies)

main()
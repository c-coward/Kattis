from sys import stdin
def main():
	k,n = map(int,stdin.readline().split())
	keyboards = []

	for i in range(k):
		line = list(map(int,stdin.readline().split()))
		keyboards.append(set(line[1:]))

	notes = list(map(int,stdin.readline().split()))

	possible = [set() for _ in range(n)]
	for i in range(n):
		for j in range(k):
			if notes[i] in keyboards[j]:
				possible[i].add(j)

	swaps = 0
	curr = set(range(k))

	for p in possible:
		curr = curr&p
		if not curr:
			curr = p
			swaps += 1

	print(swaps)

main()
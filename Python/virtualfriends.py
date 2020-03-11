from sys import stdin

def find(parents,a):
	while a != parents[a]:
		parents[a],a = parents[parents[a]],parents[a]
	return parents[a]

def union(parents,a,b):
	fa = find(parents,a)
	fb = find(parents,b)
	parents[fa] = fb

def main():
	tests = int(stdin.readline())
	for t in range(tests):
		numf = int(stdin.readline())
		parents = {}
		size = {}

		for n in range(numf):
			f1,f2 = stdin.readline().split()
			if f1 not in parents:
				parents[f1] = f1
				size[f1] = 1
			if f2 not in parents:
				parents[f2] = f2
				size[f2] = 1

			if find(parents,f1) != find(parents,f2):
				size[find(parents,f1)] += size[find(parents,f2)]
				size[find(parents,f2)] = size[find(parents,f1)]
			union(parents,f1,f2)
			print(size[find(parents,f1)])
main()
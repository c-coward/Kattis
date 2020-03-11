tests = int(input())

def find(parents,a):
	if parents[a] == a:
		return a
	parents[a] = find(parents,parents[a])
	return parents[a]

def union(parents,a,b):
	parents[find(parents,a)] = find(parents,b)

def calcDist(a,b,c,d):
	return abs(a-c) + abs(b-d)

for t in range(tests):
	storeAmt = int(input())
	places = []
	parents = [i for i in range(storeAmt + 2)]

	for s in range(storeAmt + 2):
		line = input().split()
		places.append((int(line[0]), int(line[1])))

	for i in range(storeAmt+2):
		for j in range(storeAmt+2):
			if i != j:
				distance = calcDist(places[i][0],places[i][1],places[j][0],places[j][1])
				if distance <= 1000:
					union(parents,i,j)

	if find(parents,0) == find(parents,storeAmt+1):
		print('happy')
	else:
		print('sad')
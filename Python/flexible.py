n,p = map(int,input().split())
parts = list(map(int,input().split()))

parts.insert(0,0)
parts.append(n)

possible = set()
for i in range(1,p+2):
	for j in range(i):
		possible.add(parts[i]-parts[j])

for p in sorted(possible): print(p,end=' ')
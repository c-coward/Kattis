n = int(input())
probs = []

for i in range(n):
	line = input().split()
	probs.append(float(line[1]))

probs = sorted(probs, reverse=True)
total = 0

for i in range(n):
	total += probs[i]*(i+1)

print(total)
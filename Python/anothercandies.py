from sys import stdin
t = int(input())

for i in range(t):
	input()
	n = int(stdin.readline())

	sum_ = 0
	for j in range(n):
		sum_ += int(stdin.readline())

	if not sum_ % n:
		print('YES')
	else:
		print('NO')
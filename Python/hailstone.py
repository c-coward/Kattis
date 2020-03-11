def collatz(n):
	if n == 1:
		return n;
	elif n%2 == 0:
		return n + collatz(n//2)
	else:
		return n + collatz(3*n + 1)

print(collatz(int(input())))
from sys import stdin

def main():
	t = int(stdin.readline())

	primes = sieve()

	for i in range(1,t+1):
		a,b = map(int,stdin.readline().split())
		if primes[b] and check_happy(b,set()):
			print(a,b,'YES')
		else:
			print(a,b,'NO')


def check_happy(num,seen):
	if num == 1:
		return True
	if num in seen:
		return False

	seen.add(num)

	count = 0
	while num:
		dig = num%10
		count += dig**2
		num//=10
	return check_happy(count,seen)


def sieve():
	primes = [True for _ in range(10001)]

	primes[0],primes[1] = False,False
	for i in range(10001):
		if primes[i]:
			for j in range(i**2,10001,i):
				primes[j] = False

	return primes

main()
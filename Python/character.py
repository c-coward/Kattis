from math import factorial as f
def main():
	n = int(input())

	if n <= 1:
		print(0)
	else:
		count = 0
		for i in range(2,n+1):
			count += f(n)//(f(n-i)*f(i))
		print(count)
main()
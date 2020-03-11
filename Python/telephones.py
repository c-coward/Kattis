from sys import stdin

def main():
	n,m = map(int,stdin.readline().split())

	while not (n==m==0):
		calls = []
		
		for _ in range(n):
			source,dest,start,dur = map(int,stdin.readline().split())

		for _ in range(m):
			start,dur = map(int,stdin.readline().split())

		n,m = map(int,stdin.readline().split())

main()
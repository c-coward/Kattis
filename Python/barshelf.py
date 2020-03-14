'''
Strategy: Look for the values that can be the first number in a trio
Store of the complementary value that makes up the middle for said trio
If a first was also found to be a middle, it forms a trio
This reduces the problem size from O(n^3) to O(n^2)

Recieves 2 points (n <= 5,000)
'''

def main():
	n = int(input())
	shelf = list(map(int,input().split()))

	trios = 0
	middles = {}
	for i in range(n-1):
		for j in range(i+1,n):
			if shelf[i] >= 2*shelf[j]:
				if j not in middles: middles[j] = 0
				middles[j] += 1

				# If i is a middle, j is a third
				if i in middles:
					trios += middles[i]

	print(trios)

main()
def main():
	n = int(input())

	for _ in range(n):
		k, w = input().split()
		k = int(k)

		l, r = 0, len(w) # r - l represents the length of the word after any cut

		i = 0 # Number of iterations
		# Because the word has a maximum length of 2000, the max number of iterations is relatively small (~24)

		while (r - l) >= 4: # When the length is less than 4, no letters can be taken off
			if i % 2 == 0: # Page is upside down (left side has become right side)
				l += (r - l) // 4
			else: # Page is right side up (right side is on the right)
				r -= (r - l) // 4 
			i += 1

			if i == k: # The requested number of iterations was reached
				break

		print(w[l:r])

if __name__ == '__main__':
	main()
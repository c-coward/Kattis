def main():
	string = input()
	n = len(string)

	# Check each length from 1 to n
	for i in range(1,n+1):
		if n % i: continue # Only look at divisors of n
		last = string[:i]
		found = True

		# Iterate through the rest of the string, checking each substring of length i
		for j in range(i,n,i):
			curr = string[j:j+i]

			# If string is not previous with last char swapped, exit and try next length
			if curr != last[-1] + last[:-1]:
				found = False
				break

			last = curr

		if found: return i

print(main())
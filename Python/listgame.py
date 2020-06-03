def prime_factors(n):
	f = 2 # Try all prime numbers as potential factors
	factors = 0

	while f ** 2 <= n: # Check up to the square root of the current number n
		if n % f == 0:
			factors += 1
			n //= f # As all instances of f are factored out, the next largest prime factor will be the next factor checked
		else:
			f += 1 # Repeats this block untill a prime factor is reached

	return factors + 1 # Add one to account for final prime factor not reached in the loop

print(prime_factors(int(input())))
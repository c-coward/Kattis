def main():
	n = int(input())
	# Iterate until either == 0
	while ((n % 8) and ((n-5) % 8)):
		n += 1
	print(n)

main()
def main():
	n = int(input())

	i = 0
	complement = 0
	while i < n:
		complement = round((n + i*i)**.5)
		if complement*complement - i*i == n:
			print(i,complement)
			return

		i += 1
	print('impossible')

main()
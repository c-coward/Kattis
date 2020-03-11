def main():
	string = input()
	letters = {}

	for l in string:
		if l not in letters: letters[l] = 0
		letters[l] += 1

	count = len(letters)

	if count <= 2:
		print(0)
	else:
		subs = 0
		for letter in sorted(letters,key = lambda x:letters[x]):
			count -= 1
			subs += letters[letter]
			if count <= 2:
				subs -= (2-count)
				break

		print(subs)

main()
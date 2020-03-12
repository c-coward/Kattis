def main():
	num_letters,num_words = map(int,input().split())
	letters = {}

	for _ in range(num_letters):
		a,b = input().split()
		if a not in letters: letters[a] = set()
		letters[a].add(b)

	for _ in range(num_words):
		word1,word2 = input().split()

		if word1 == word2:
			print('yes')
		elif len(word1) != len(word2):
			print('no')
		else:
			found = True
			for i in range(len(word1)):
				if not dict_traverse(letters,word1[i],word2[i],set()):
					found = False
					break
			print('yes' if found else 'no')

def dict_traverse(letters,start,end,seen):
	seen.add(start)

	if start == end:
		return True

	if start not in letters:
		return False

	for char in letters[start]:
		if char in seen: continue

		if dict_traverse(letters,char,end,seen):
			return True

	return False

main()
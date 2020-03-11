from sys import stdin

words = []
longest = 0
for line in stdin:
	l = line.strip()
	if l == '':
		words.sort()
		for w in words:
			print((longest-len(w))*' ' + w[::-1])
		longest = 0
		words = []
		print()
		continue

	words.append(l[::-1])
	if len(l) > longest: longest = len(l)

words.sort()
for w in words:
	print((longest-len(w))*' ' + w[::-1])
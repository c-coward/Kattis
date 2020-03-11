from math import factorial as f
try:
	while 1:
		word = input()
		nfac = f(len(word))
		letters = {w:0 for w in word}
		for w in word:
			letters[w] += 1
		for l in letters:
			nfac //= letters[l]
		print(nfac)
except:
	pass
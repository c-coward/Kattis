word = input()
e = int(input())
soundslike = []
for i in range(e):
	mightsound = input().split()
	for i in range(len(word)):
		if word[i:] in mightsound:
			soundslike += mightsound
			break
p = int(input())
for i in range(p):
	line = input()
	rhymes = False
	for s in soundslike:
		n = len(s)
		if s == line[-n:]:
			rhymes = True
			break
	print(["NO","YES"][rhymes])
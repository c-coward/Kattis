from math import ceil
def main():
	l,w = map(int,input().split())

	if not (1 <= w/l <= 26):
		print('impossible')
		return

	minw = ceil(w/l)
	string = []
	while minw != w/l:
		string.append(chr(96+minw))
		w -= minw
		l -= 1
		if not l: break
		minw = ceil(w/l)
	string.append(chr(96+minw)*l)

	print(''.join(string))

main()
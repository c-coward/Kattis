def main():
	n = int(input())
	seats = list(map(int,input().split()))

	awkwardness = n

	langs = {}
	for i in range(n):
		curr = seats[i]
		if curr not in langs: langs[curr] = []
		langs[curr].append(i)

	if len(langs) == n:
		print(n)
		return

	for lang in langs:
		indices = langs[lang]
		for i in range(1,len(indices)):
			diff = indices[i]-indices[i-1]
			if diff < awkwardness: awkwardness = diff

	print(awkwardness)

main()
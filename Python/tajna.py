word = input()
arr = [i for i in range(1,int(len(word)**.5) + 1) if len(word) % i == 0]
r = arr[-1]
c = len(word)//(arr[-1])

output = ''
for i in range(r):
	for j in range(c):
		print(word[r*j+i],end='')
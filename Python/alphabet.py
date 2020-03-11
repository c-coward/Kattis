string = input()
lis = [1]*len(string)
i = 1

while i < len(string):
	for j in range(i):
		if (string[i] > string[j] and lis[i] < lis[j] + 1):
			lis[i] = lis[j] + 1
	i += 1

m = 1
for l in lis:
	if l > m: m = l

print(26 - m)
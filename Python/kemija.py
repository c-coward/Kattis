string = input()
n = len(string)
i = 0

while i < n:
	if string[i] in 'aeiou':
		string = string[:i+1] + string[i+3:]
		n -= 2
	i += 1

print(string)
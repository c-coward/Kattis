word = input()
white = 0
upper = 0
lower = 0
symbol = 0

for char in word:
	if char == "_":
		white += 1
	elif char in "abcdefghijklmnopqrstuvwxyz":
		lower += 1
	elif char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		upper += 1
	else:
		symbol += 1

print(white/len(word))
print((lower/len(word)))
print((upper/len(word)))
print((symbol/len(word)))
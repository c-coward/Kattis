guess = 500
upper = 1001
lower = 1

print(guess)
answer = input()
while answer != 'correct':
	if answer == 'higher':
		lower = guess
	else:
		upper = guess
	guess = (upper + lower)//2
	print(guess)
	answer = input()
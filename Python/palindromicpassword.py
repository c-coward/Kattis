n = int(input())
for i in range(n):
	password = input()
	pass1 = password[:3] + password[2::-1]
	pass2 = password[:2] + str(int(password[2]) + 1)*2 + password[1::-1]
	pass3 = password[:2] + str(int(password[2]) - 1)*2 + password[1::-1]
	diff1 = abs(int(password) - int(pass1))
	diff2 = abs(int(password) - int(pass2))
	diff3 = abs(int(password) - int(pass3))
	if (diff1 < diff2 and diff1 < diff3):
		print(pass1)
	elif diff2 < diff3:
		print(pass2)
	else:
		print(pass3)
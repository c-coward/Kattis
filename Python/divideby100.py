n = input()
m = input()

ln, lm = len(n), len(m) - 1

# Remove trailing zeroes
trail = 0
for i in range(ln - 1, -1 , -1):
	if lm - trail == 0:
		break

	if n[i] == '0':
		trail += 1
	else:
		break

n = n[ : ln - trail]
m = m[ : lm - trail]
ln -= trail
lm -= trail

if lm == 0:
	print(n)
elif ln == lm:
	print('0.' + n)
elif ln > lm:
	print(n[ : ln - lm] + '.' + n[ ln - lm : ])
else:
	print('0.' + '0' * (lm - ln) + n)
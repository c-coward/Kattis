input()

bacteria = 1
for e in map(int,input().split()):
	bacteria *= 2
	bacteria -= e
	if bacteria < 0:
		break

if bacteria < 0:
	print('error')
else:
	print(bacteria % (10**9+7))
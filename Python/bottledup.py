def main():
	oil,v1,v2 = map(int,input().split())

	b1 = oil//v1
	oil -= v1*b1

	while oil%v2 != 0:
		oil += v1
		b1 -= 1
		if b1 < 0: break

	b2 = oil//v2

	if b1 < 0:
		print("Impossible")
	else:
		print(b1,b2)

main()
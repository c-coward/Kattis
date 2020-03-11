line = input().split(" ")
a1 = int(line[0])
a2 = int(line[1])

if a1 == 0 and a2 == 0:
	print("Not a moose")
elif a1 == a2:
	print("Even",a1+a2)
elif a1 > a2:
	print("Odd",a1*2)
else:
	print("Odd",a2*2)
n = int(input())
test = 1
while n != 0:
	print("List " + str(test) + ":")
	animals = {}
	for i in range(n):
		line = input().split(" ")
		animal = line[len(line)-1].lower()
		if animal in animals:
			animals[animal] += 1
		else:
			animals[animal] = 1

	sortan = sorted(animals)

	for n in sortan:
		print(n + " | " + str(animals[n]))

	test += 1
	n = int(input())
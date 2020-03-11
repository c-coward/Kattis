line = input().split(" ")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while line[0] is not "0":
	num = int(line[0])
	string = line[1]
	newstr = ""

	for char in string:
		newstr += letters[(letters.index(char) + num) % 28]

	print(newstr[::-1])

	line = input().split(" ")
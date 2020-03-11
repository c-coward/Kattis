n = int(input())

for i in range(n):
	line = input()
	output = ""
	for l in "abcdefghijklmnopqrstuvwxyz":
		if l not in line.lower():
			output += l

	if output == "":
		print("pangram")
	else:
		print("missing",output)
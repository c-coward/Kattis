name = [i for i in input()]

i = 0
while i < len(name)-1:
	if name[i] == name[i+1]:
		name.pop(i+1)
	else:
		i+=1
for i in name:
	print(i, end = "")
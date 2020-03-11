tests = int(input())

accept = []

for t in range(tests):
	items = int(input())
	name = input()
	dishes = [input() for i in range(items)]
	f1 = False
	f2 = False
	for d in dishes:
		if d == "pea soup":
			f1 = True
		elif d == "pancakes":
			f2 = True
	if f1 and f2:
		accept.append(name)

if len(accept) == 0:
	print("Anywhere is fine I guess")
else:
	print(accept[0])
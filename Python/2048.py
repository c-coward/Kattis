line1 = input().split(" ")
line2 = input().split(" ")
line3 = input().split(" ")
line4 = input().split(" ")
direction = int(input())
lines = [line1,line2,line3,line4]
aaa = lines
for i in range(4):
	for j in range(4):
		aaa[i][j] = int(lines[i][j])

def move(d,board):
	b = []
	if d == 0 :
		# left
		for n in board:
			a = [i for i in n if i != 0]
			j = 0
			while j < len(a)-1:
				if a[j] == a[j+1]:
					a[j] *= 2
					a.remove(a[j+1])
				j += 1
			b = a + [0]*(4-len(a))
			for i in range(4):
				print(b[i],end=" ")
			print()

	if d == 2:
		# right
		for n in board:
			a = [i for i in n if i != 0]
			j = len(a)-1
			while j > 0:
				if a[j] == a[j-1]:
					a[j] *= 2
					a.remove(a[j-1])
					j -= 1
				j -= 1
			b = [0]*(4-len(a)) + a
			for i in range(4):
				print(b[i],end=" ")
			print()

	if d == 1:
		# up
		arr = []
		for i in range(4):
			a = [n[i] for n in board if n[i] != 0]
			j = 0
			while j < len(a)-1:
				if a[j] == a[j+1]:
					a[j] *= 2
					a.remove(a[j+1])
				j += 1
			b = a + [0]*(4-len(a))
			arr.append(b)
		for k in range(4):
			for m in arr:
				print(m[k],end=" ")
			print()

	if d == 3:
		# down
		arr = []
		for i in range(4):
			a = [n[i] for n in board if n[i] != 0]
			j = len(a)-1
			while j > 0:
				if a[j] == a[j-1]:
					a[j] *= 2
					a.remove(a[j-1])
					j -= 1
				j -= 1
			b = [0]*(4-len(a)) + a
			arr.append(b)
		for k in range(4):
			for m in arr:
				print(m[k],end=" ")
			print()

move(direction,aaa)
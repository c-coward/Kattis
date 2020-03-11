ins = [int(i) for i in input().split()]
rows,cols,size = ins[0],ins[1],ins[2]
window = [input() for i in range(rows)]
rows,cols = rows-size+1,cols-size+1

flies = []
for i in range(rows):
	for j in range(cols):
		tot = 0
		for w in window[i+1:i+size-1]:
			tot += sum(1 for c in w[j+1:j+size-1] if c == '*')
		flies.append(tot)

largest = 0
index = 0
for f in range(len(flies)):
	if flies[f] > largest:
		largest = flies[f]
		index = f
r = index//cols
c = index%cols

newWindow = window[0:r]
for i in range(size):
	newRow = window[r+i][0:c]
	if (i == 0 or i == size-1):
		newRow += '+' + '-'*(size-2) + '+'
	else:
		newRow += '|' + ''.join(window[r+i][c+1:c+size-1]) + '|'
	newRow += window[r+i][c+size:]
	newWindow.append(newRow)
newWindow += window[r+size:]

print(largest)
for nw in newWindow:
	print(nw)
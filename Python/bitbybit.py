instructions = int(input())

while instructions != 0:
	bits = ['?']*32
	for i in range(instructions):
		ins = input().split(' ')
		if ins[0] == 'SET':
			bits[31-int(ins[1])] = '1'
		elif ins[0] == 'CLEAR':
			bits[31-int(ins[1])] = '0'
		elif ins[0] == 'OR':
			if (bits[31-int(ins[1])] == '1') or (bits[31-int(ins[2])] == '1'):
				bits[31-int(ins[1])] = '1'
			elif (bits[31-int(ins[1])] == "?") or (bits[31-int(ins[2])] == "?"):
				bits[31-int(ins[1])] = "?"
			else:
				bits[31-int(ins[1])] = '0'
		elif ins[0] == 'AND':
			if (bits[31-int(ins[1])] == '0') or (bits[31-int(ins[2])] == '0'):
				bits[31-int(ins[1])] = '0'
			elif bits[31-int(ins[1])] != bits[31-int(ins[2])]:
				bits[31-int(ins[1])] = '?'



	print(''.join(bits))
	instructions = int(input())
outs = []
for i in range(1,6):
	blimp = input()
	if 'FBI' in blimp: outs.append(str(i))
print(' '.join(outs) if outs else 'HE GOT AWAY!')
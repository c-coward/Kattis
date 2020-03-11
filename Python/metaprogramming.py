from sys import stdin
words = {}
outs = []
for line in stdin:
	line = line.strip().split()
	if line[0] == 'define':
		words[line[2]] = int(line[1])
	else:
		if (line[1] not in words or line[3] not in words):
			outs.append('undefined')
		elif line[2] == '=':
			outs.append(str(words[line[1]] == words[line[3]]).lower())
		elif line[2] == '>':
			outs.append(str(words[line[1]] > words[line[3]]).lower())
		else:
			outs.append(str(words[line[1]] < words[line[3]]).lower())
print('\n'.join(outs))
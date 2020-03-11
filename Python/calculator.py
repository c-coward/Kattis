from sys import stdin

outs = []
for line in stdin:
	ev = eval(line)
	outs.append("%.2f" % ev)
print('\n'.join(outs))
from math import log
from sys import stdin

outs = []
for line in stdin:
    line = line.strip()
    if line == 'END':
        break

    n = len(line)

    if line == '1':
        outs.append('1')
    elif n == 1:
        outs.append('2')
    elif n < 10:
        outs.append('3')
    else:
        outs.append('4')


print('\n'.join(outs))

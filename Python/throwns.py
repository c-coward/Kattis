k,c = map(int,input().split())
commands = input().split()
i = 0
while i < c:
	if commands[i] == 'undo':
		n = int(commands[i+1])
		commands = commands[:i-n] + commands[i+2:]
		i -= n+1
		c -= n+1
	i += 1

pos = 0
for c in commands:
	pos += int(c)
print(pos%k)
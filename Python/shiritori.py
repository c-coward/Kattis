from sys import stdin

n = int(input())

said = set()
word = input()
said.add(word)
last = word[-1]
p = 2
fair = True

for line in stdin:
	line = line.strip()

	if line in said or line[0] != last:
		fair = False
		break

	said.add(line)
	last = line[-1]

	if p == 1:
		p = 2
	else:
		p = 1

if fair:
	print("Fair Game")
else:
	print("Player",p,"lost")
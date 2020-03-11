ins = [int(i) for i in input().split(" ")]
players = {input():0 for i in range(ins[0])}
for i in range(ins[2]):
	line = input().split(" ")
	players[line[0]] += int(line[1])

winners = [p for p in players if players[p] >= ins[1]]
if len(winners) == 0:
	print("No winner!")
else:
	for w in winners:
		print(w,'wins!')
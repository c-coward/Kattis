line = input()
votes = {}
while line != "***":
	if line in votes:
		votes[line] += 1
	else:
		votes[line] = 0
	line = input()

mostVotes = -1
winner = ''

for n in votes:
	if votes[n] == mostVotes:
		mostVotes = -1
		break
	elif votes[n] > mostVotes:
		mostVotes = votes[n]
		winner = n
if mostVotes != -1:
	print(winner)
else:
	print('Runoff!')
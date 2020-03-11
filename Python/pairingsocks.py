n = int(input())
pile = list(reversed(input().split()))
aux = [pile.pop()]

moves = 1
pairs = 0

while pile:
	if not aux:
		aux.append(pile.pop())
		moves += 1
	if aux[-1] != pile[-1]:
		aux.append(pile.pop())
	else:
		aux.pop()
		pile.pop()
		pairs += 1

	moves += 1

print("impossible" if pairs != n else moves)
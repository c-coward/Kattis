from collections import deque
def main():
	t = int(input())

	for _ in range(t):
		goal = input()
		best = float('inf')

		q = deque()
		q.append((0,input()))
		q.append((1,input()))
		q.append((1,input()))
		q.append((1,input()))

		while q:
			dist,word = q.popleft()
			i = 0
			while i < len(word) and i < len(goal):
				if word[i] != goal[i]: break
				i += 1
			presses = dist + len(word) + len(goal) - 2*i
			best = min(presses,best)

		print(best)
main()
from collections import deque

'''
Solution to the moneymatters problem on kattis.
As not all persons are friends with each other, multiple graphs can exist among these persons.
A DFS is used to visit every node in a graph and ensure that all debts in that graph can be paid.

Originally a recursive DFS was implemented, but the problem size (50,000 connections) caused the
max depth limit to be reached.
'''
def main():
	n, m = map(int, input().split())
	debts = [int(input()) for _ in range(n)]

	friends = [set() for _ in range(n)]
	for _ in range(m):
		u, v = map(int, input().split())

		friends[u].add(v)
		friends[v].add(u)

	visited = [False for _ in range(n)]

	stack = deque()
	# Find all separate graphs in this group of people
	for i in range(n):
		# Don't check people in previously visited graphs
		if visited[i]:
			continue

		visited[i] = True
		stack.append(i)

		tot = 0
		# Visit every person in the same graph as this person
		while stack:
			index = stack.pop()
			# Add up all of the debts in this graph
			tot += debts[index]

			for friend in friends[index]:
				# Don't revisit friends in the graph
				if not visited[friend]:
					visited[friend] = True
					stack.append(friend)

		# If this graph couldn't equalize the debt, it is a failure
		if tot != 0:
			print("IMPOSSIBLE")
			return

	# If all networks of friends could repay the debts, it is a success
	print("POSSIBLE")

if __name__ == '__main__':
	main()
from collections import deque

def main():
	delims = {'}': '{', ']': '[', ')': '('}

	n = int(input())
	exp = input()
	stack = deque()
	for i in range(n):
		if exp[i] in delims:
			if not stack or stack.pop() != delims[exp[i]]:
				return f'{exp[i]} {i}'
		elif exp[i] != ' ':
			stack.append(exp[i])

	return 'ok so far'

print(main())
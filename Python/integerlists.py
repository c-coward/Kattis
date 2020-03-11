from collections import deque

def main():
	test_cases = int(input())
	for _ in range(test_cases):
		instructions = input()
		length = int(input())
		nums = deque(input()[1:-1].split(','))
		if nums == deque(['']): nums = deque()

		left = True
		try:
			for i in instructions:
				if i == 'R':
					left = not left
				else:
					if left:
						nums.popleft()
					else:
						nums.pop()

			if left:
				print('[' + ','.join(nums) + ']')
			else:
				nums.reverse()
				print('[' + ','.join(nums) + ']')
		except:
			print('error')

main()
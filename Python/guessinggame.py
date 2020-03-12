from sys import stdin

def main():
	lower = -1
	higher = 11
	n = int(stdin.readline())
	honest = True
	while n:
		info = stdin.readline().strip()
		if info == 'too high':
			if n < lower:
				honest = False
			elif n < higher:
				higher = n
		elif info == 'too low':
			if n > higher:
				honest = False
			elif n > lower:
				lower = n
		elif info == 'right on':
			if not (lower < n < higher):
				honest = False

			if not honest:
				print('Stan is dishonest')
			else:
				print('Stan may be honest')
			lower = -1
			higher = 11
			honest = True

		n = int(stdin.readline())

main()
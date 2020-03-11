from sys import stdin

def main():
	answers = find_perms()
	t = int(stdin.readline())

	for _ in range(t):
		to_find = int(stdin.readline())
		print(answers[to_find] if to_find in answers else 'no solution')

def find_perms():
	answers = {}
	ops = '+-/*'

	for o1 in ops:
		for o2 in ops:
			for o3 in ops:
				exp = '4 %s 4 %s 4 %s 4' % (o1,o2,o3)

				t1 = o1 if o1 != '/' else '//'
				t2 = o2 if o2 != '/' else '//'
				t3 = o3 if o3 != '/' else '//'

				to_eval = '4 %s 4 %s 4 %s 4' % (t1,t2,t3)

				result = eval(to_eval)
				checker = eval(exp)

				if checker == result: answers[result] = (exp + ' = ' + str(result))

	return answers

if __name__ == '__main__': main()
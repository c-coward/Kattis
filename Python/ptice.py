def main():
	a = 'ABC'
	b = 'BABC'
	g = 'CCAABB'

	n = int(input())
	correct = input()

	ac,bc,gc = 0,0,0
	for i in range(n):
		if correct[i] == a[i%3]: ac += 1
		if correct[i] == b[i%4]: bc += 1
		if correct[i] == g[i%6]: gc += 1

	best = max(ac,bc,gc)
	print(best)
	if ac == best: print('Adrian')
	if bc == best: print('Bruno')
	if gc == best: print('Goran')

if __name__ == '__main__': main()
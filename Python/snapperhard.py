from sys import stdin
def main():
	tests = int(stdin.readline())
	outs = []
	for t in range(tests):
		snappers,snaps = map(int,stdin.readline().split())
		snaps += 1
		on = 'OFF'
		if snaps % 2**snappers == 0:
			on = 'ON'
		outs.append('Case #%d: %s' % (t+1,on))
	print('\n'.join(outs))

if __name__ == "__main__": main()
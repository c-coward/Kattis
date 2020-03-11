from sys import stdin

def main():
	trees = {}
	count = 0

	for line in stdin:
		tree = line.strip()
		if tree not in trees: trees[tree] = 0
		trees[tree] += 1
		count += 1

	outs = []
	for tree in sorted(trees):
		outs.append(f'{tree} {trees[tree]/count*100}')
	print('\n'.join(outs))

main()
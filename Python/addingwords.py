from sys import stdin

words = {}

def calc(nums,ops):
	if len(nums) == 1:
		if nums[0] in words: return ' ' + nums[0]
		return ' unknown'
	tocalc = []
	for n in nums:
		if n not in words: return ' unknown'
		tocalc.append(words[n])

	exp = ('%d' + '%d'.join(ops) + '%d') % tuple(tocalc)
	calculated = eval(exp)
	
	vals = {words[w]:w for w in words}
	if calculated not in vals: return ' unknown'
	return ' ' + vals[calculated]

outs = []

for line in stdin:

	line = line.strip().split()
	command = line[0]
	args = line[1:]

	if command == 'def':
		if int(args[1]) not in words.values():
			words[args[0]] = int(args[1])

	elif command == 'calc':
		end = calc(args[0::2],args[1:len(args)-1:2])
		outs.append(' '.join(args) + end)

	else:
		words = {}

print('\n'.join(outs))
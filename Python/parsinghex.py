from sys import stdin

def main():
	stream = ''.join(stdin.readlines())

	hexes = []
	seen_0,seen_x = False,False
	curr = []

	for char in stream:
		if seen_x:
			if char.lower() in '1234567890abcdef':
				curr.append(char)
				
			else:
				hexes.append(''.join(curr))
				curr = []
				seen_0,seen_x = False,False

		elif seen_0:
			if char in 'xX':
				seen_x = True
				curr.append(char)

			else:
				seen_0 = False
				curr = []

		elif char == '0':
			seen_0 = True
			curr.append(char)

	for string in hexes:
		print(string,int(string,16))

main()
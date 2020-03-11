def main():
	translations = {'at': '@', 'and': '&', 'one': '1', 'won': '1', 'to': '2', 'too': '2', 'two': '2', 'for': '4', 'four': '4', 'be': 'b', 'bea': 'b', 'bee': 'b', 'sea': 'c', 'see': 'c', 'eye': 'i', 'oh': 'o', 'owe': 'o', 'are': 'r', 'you': 'u', 'why': 'y'}

	n = int(input())
	for _ in range(n):
		instr = input()
		outp = []
		i = 0
		while i < len(instr):
			if i <= len(instr)-4:
				if instr[i:i+4].lower() in translations:
					to_add = translations[instr[i:i+4].lower()]
					if instr[i].isupper():
						to_add = to_add[0].upper() + to_add[1:]

					outp.append(to_add)
					i += 4
					continue

			if i <= len(instr)-3:
				if instr[i:i+3].lower() in translations:
					to_add = translations[instr[i:i+3].lower()]
					if instr[i].isupper():
						to_add = to_add[0].upper() + to_add[1:]

					outp.append(to_add)
					i += 3
					continue

			if i <= len(instr)-2:
				if instr[i:i+2].lower() in translations:
					to_add = translations[instr[i:i+2].lower()]
					if instr[i].isupper():
						to_add = to_add[0].upper() + to_add[1:]

					outp.append(to_add)
					i += 2
					continue

			outp.append(instr[i])
			i += 1

		print(''.join(outp))

main()
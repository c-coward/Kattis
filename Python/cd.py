from sys import stdin

def main():
	jai,jii = map(int,stdin.readline().split())

	while not (jai==jii==0):
		jaset = {stdin.readline().strip() for _ in range(jai)}
		jiset = {stdin.readline().strip() for _ in range(jii)}

		print(len(jaset & jiset))
		jai,jii = map(int,stdin.readline().split())

main()
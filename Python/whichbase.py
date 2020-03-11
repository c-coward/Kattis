def main():
	k = int(input())
	for _ in range(k):
		t,n = map(int,input().split())

		try:
			oc = int(f'0o{n}', 8)
		except:
			oc = 0

		he = int(f'0x{n}',16)

		print(t,oc,n,he)

main()
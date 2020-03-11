ins = [int(i) for i in input().split(" ")]
broken = [int(i) for i in input().split(" ")]
reserve = [int(i) for i in input().split(" ")]
resCheck = reserve.copy()
brokCheck = broken.copy()

for r in reserve:
	for b in broken:
		if (r == b + 1 or r == b - 1) and (r in resCheck) and (b in brokCheck):
			resCheck.remove(r)
			brokCheck.remove(b)

print(len(brokCheck))
n = int(input())
slats = {'TB':0,'LR':0}
for i in range(n):
	sword = input()
	if sword[0] == '0':
		slats['TB'] += 1
	if sword[1] == '0':
		slats['TB'] += 1
	if sword[2] == '0':
		slats['LR'] += 1
	if sword[3] == '0':
		slats['LR'] += 1

TB = slats['TB']
LR = slats['LR']
tb = TB//2
lr = LR//2
swords = 0

if tb > lr:
	swords = lr
else:
	swords = tb

TB -= swords*2
LR -= swords*2
print(swords,TB,LR)
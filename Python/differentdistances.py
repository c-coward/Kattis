from sys import stdin

def dist(a,b,c,d,n):
	return (abs(a-c)**n + abs(b-d)**n)**(1/n)

for l in stdin:
	if l.strip() == '0':
		break
	x1,y1,x2,y2,p = [float(i) for i in l.strip().split()]

	print(dist(x1,y1,x2,y2,p))
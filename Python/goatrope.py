from math import hypot

def main():
	x,y,x1,y1,x2,y2 = map(int,input().split())
	points = ((x1,y1),(x1,y2),(x2,y1),(x2,y2))
	if x1<=x<=x2:
		print(min(abs(y-y1),abs(y-y2)))
	elif y1<=y<=y2:
		print(min(abs(x-x1),abs(x-x2)))
	else:
		dist = float('inf')
		for i,j in points:
			dist = min(dist,hypot(x-i,y-j))
		print(dist)

main()
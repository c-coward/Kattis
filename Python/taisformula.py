from sys import stdin

def main():
	stdin.readline()
	t1,v1 = map(float,stdin.readline().strip().split())
	s = 0

	for line in stdin:
		t,v = map(float,line.strip().split())
		s += (t-t1)*(v+v1)/2
		t1,v1 = t,v

	print(s/1000)

if __name__ == '__main__': main()
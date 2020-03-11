from math import floor
def main():
	n = int(input())
	coeffs = list(map(int,input().split()))

	num = 1
	denom = coeffs[-1]
	for x in coeffs[-2::-1]:
		denom,num = fradd(x,num,denom)
	
	gcf_ = gcf(denom,num)
	print(f'{denom//gcf_}/{num//gcf_}')

def fradd(whole,num,denom):
	return whole*denom + num, denom

def gcf(x,y):
	while(y):
		x,y = y,x%y
	return x

main()
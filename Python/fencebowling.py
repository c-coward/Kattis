from math import atan,pi

'''
Explanation of the math:
	Note: _ is used to denote subscripts
	Each bounce results in a new angle A_n, from n=0 to n=k
	A_0 = Beta, the angle we're solving for
	A_n = atan(2 * tan( A_(n-1) ))

	Due to the recursive nature, all angles can be expressed in this way:
		A_n = atan(2^n * tan(A_0))
		tan(A_n) = 2^n * tan(A_0)

	The length of the hall, L, can be expressed as the sum of Y components
		L = sum(Y_n for n in range(k))

	Since tan(A_n) = Y_n/X_n: Y_n = X_n * tan(A_n)
	Using the general form: Y_n = X_n * 2^n * tan(A_0)

	X_n will either be w/2 (for n = 0,k) or w (for n from 1 to k-1)
	
	Let the variable C = the sum of these widths

	Thus: L = C * tan(A_0)

	and A_0 = atan(L/C)

	Special Case:
		if k = 0: no bounces occur, so the initial angle was 90 degrees
'''

def main():
	k,w,L = map(int,input().split())

	C = w * ( .5 + sum(2**n for n in range(1,k)) + 2**(k-1) )
	# k-1 is repeated because 2**k is divided by 2

	beta = atan(L/C)/pi*180 # Must be converted to degrees

	if k:
		print(beta)
	else:
		print(90)

main()

from math import pi
nums = [float(i) for i in input().split(" ")]
if nums[0] <= pi*(nums[1]/(2*pi))**2:
	print('Diablo is happy!')
else:
	print('Need more materials!')

"""
A = piR**2
C = 2piR
R = C/(2pi)
A = pi(C/2pi)**2
"""

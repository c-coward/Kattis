from math import e

fracts = [0, 1.0, .5, .66666666666, .625, .6333333333, .63194444, .6321428571, .632118055, .6321208112]

n = int(input())

if n < 10:
	print(fracts[n])
else:
	print(1-1/e)
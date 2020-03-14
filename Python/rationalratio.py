def main():
	num,repeats = input().split()
	whole,decimal = num.split('.')
	repeats = int(repeats)

	nonrepeating_numerator = decimal[:-repeats]
	nonrepeating_denominator = 10**(len(decimal)-repeats)

	repeating_numerator = decimal[-repeats:]
	repeating_denominator = (10**repeats -1) * nonrepeating_denominator

	if nonrepeating_numerator == '': nonrepeating_numerator = '0'

	total = (int(whole)*repeating_denominator
			+ int(nonrepeating_numerator)*repeating_denominator//nonrepeating_denominator
			+ int(repeating_numerator))

	factor = gcf(total,repeating_denominator)

	print(f'{total//factor}/{repeating_denominator//factor}')

def gcf(a,b):
	while b != 0:
		a,b = b,a%b
	return a

main()
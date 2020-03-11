line = [int(i) for i in input().split()]

print('yes' if 2**(line[1]+1) - 1 >= line[0] else 'no')
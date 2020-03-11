n = int(input())
binN = bin(n)[2:]
Nnib = binN[-1::-1]
print(int('0b'+Nnib,2))
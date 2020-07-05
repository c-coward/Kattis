b,k,g = map(int, input().split())
print((b - 1) // (k // g) + (((b - 1) // (k // g)) * (k // g) < (b - 1)))
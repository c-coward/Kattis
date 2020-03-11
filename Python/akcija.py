n = int(input())

books = []

for i in range(n):
	books.append(int(input()))

b = sorted(books)

backb = [b[i] for i in range(n-1,-1,-1)]

price = 0

for i in range(n):
	if i % 3 != 2:
		price += backb[i]

print(price)
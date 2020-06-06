def main():
	n = int(input())

	for _ in range(n):
		k, w = map(int, input().split())
		words = [input() for _ in range(w)]

		base = words[0]
		for i in range(1, w):
			base = lineup(base, words[i], k)

		print(len(base))

def lineup(word1, word2, k):
	for i in range(k):
		if word1[i + len(word1) - k:] == word2[:k - i]:
			return word1[:i + len(word1) - k] + word2

	return word1 + word2

if __name__ == '__main__':
	main()
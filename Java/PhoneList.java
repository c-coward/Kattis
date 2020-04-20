import java.util.Scanner;

public class PhoneList {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		int t = in.nextInt();
		for (int i = 0; i < t; i++) {
			int n = in.nextInt();
			Trie nums = new Trie();
			boolean yes = true;

			for (int j = 0; j < n; j++) {
				String num = in.next();

				if (yes && !nums.add(num)){
					yes = false;
				}
			}

			System.out.println(yes ? "YES" : "NO");
		}
	}

	// A Trie data structure is used as it makes it very simple to check if one value is a prefix of another
	private static class Trie {
		public Node root;

		public Trie() {
			this.root = new Node();
		}

		// Returns false if the phone number causes the set to be invalid
		public boolean add(String num) {
			Node n = this.root;

			for (int i = 0; i < num.length(); i++) {
				// If a finished number is reached, this number contains a prefix
				if (n.isNum) return false;

				int index = num.charAt(i) - '0';

				if (n.c[index] == null) {
					n.c[index] = new Node();
				} else if (i == num.length() - 1) {
					// If the last node in this number is not a new node, it is a prefix of another number
					return false;
				}

				n = n.c[index];
			}

			n.isNum = true;
			return true;
		}
	}

	private static class Node {
		public Node[] c;
		public boolean isNum;

		public Node() {
			isNum = false;
			this.c = new Node[10];
		}
	}

}
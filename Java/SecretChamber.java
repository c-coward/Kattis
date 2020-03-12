import java.util.*;
public class SecretChamber {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int letters = scan.nextInt();
		int words = scan.nextInt();
		HashMap<Character, HashSet<Character>> dict =
			new HashMap<Character, HashSet<Character>>();

		for (int i = 0; i < letters; i++) {
			char l1 = scan.next().charAt(0);
			char l2 = scan.next().charAt(0);
			HashSet<Character> temp;
			if (dict.containsKey(l1)) {
				temp = dict.get(l1);
			} else {
				temp = new HashSet<Character>();
			}
			temp.add(l2);
			dict.put(l1,temp);
		}

		for (int i = 0; i < words; i++) {
			String word1 = scan.next();
			String word2 = scan.next();

			if (word1.equals(word2)) {
				System.out.println("yes");

			} else if (word1.length() != word2.length()) {
				System.out.println("no");

			} else {
				boolean[] found = new boolean[word1.length()];

				for (int j = 0; j < word1.length(); j++) {
					char char1 = word1.charAt(j);
					char char2 = word2.charAt(j);
					Queue<Character> q =
						new LinkedList<Character>();

					if (char1 == char2) {
						found[j] = true;
						continue;
					}

					q.add(char1);
					HashSet<Character> visited = new HashSet<Character>();

					while (!q.isEmpty()) {
						char curr = q.poll();
						if (curr == char2) {
							found[j] = true;
							continue;
						}
						if (visited.contains(curr)) {
							continue;
						}
						visited.add(curr);
						if (!dict.containsKey(curr)) {
							continue;
						}
						HashSet<Character> points = dict.get(curr);
						for (char c : points) {
							q.add(c);
						}
					}
				}

				boolean doPrint = true;
				for (boolean b : found) {
					if (b == false) {
						doPrint = false;
					}
				}
				System.out.println(doPrint ? "yes" : "no");
			}
		}
	}
}
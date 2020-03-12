import java.util.*;

public class Shiritori {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<String> words = new ArrayList<String>();
		HashSet<String> wordSet = new HashSet<String>();
		int n = Integer.parseInt(scan.nextLine());
		int player = 0;
		for (int i = 0; i < n; i++) {
			String word = scan.nextLine();
			words.add(word);
			if (i > 0) {
				if (words.get(i).charAt(0) != words.get(i-1).charAt(words.get(i-1).length() - 1)) {
					player = (i % 2) + 1;
					break;
				}
			}
			if (wordSet.contains(words.get(i))) {
				player = (i % 2) + 1;
				break;
			} else {
				wordSet.add(word);
			}
		}
		if (player == 0) {
			System.out.println("Fair Game");
		} else {
			System.out.println("Player " + player + " lost");
		}
	}
}
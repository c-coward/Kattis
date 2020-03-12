import java.util.*;

public class BabyBites {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);

		int n = scan.nextInt();
		scan.nextLine();
		String[] words = scan.nextLine().split(" ");
		boolean sense = true;

		for (int i = 0; i < words.length; i++) {
			if (sense) {
				try {
					if(Integer.parseInt(words[i]) - 1 != i) {
						sense = false;
					}
				} catch(NumberFormatException e) {
					;
				}
			}
		}

		if (!sense) {
			System.out.println("something is fishy");
		} else {
			System.out.println("makes sense");
		}
	}
}
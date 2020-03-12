import java.util.*;

public class Palindromic {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int n = scan.nextInt();

		for (int i = 0; i < n; i++) {
			int line = scan.nextInt();
			int result = -1;
			int diff = 0;
			while (result == -1) {
				if (isPalindrome(line - diff)) {
					result = line - diff;
				} else if (isPalindrome(line + diff)) {
					result = line + diff;
				}
				diff++;
			}
			System.out.println(result);
		}
	}

	static boolean isPalindrome(int numberS) {
		String number = Integer.toString(numberS);
		if (number.length() != 6) {
			return false;
		}
		return (number.charAt(0) == number.charAt(5) && number.charAt(1) == number.charAt(4) && number.charAt(2) == number.charAt(3));
	}
}
import java.util.*;

public class BlackFriday {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		scan.nextLine();
		String rolls = scan.nextLine();
		int x = rolls.length();
		int num1 = x - rolls.replace("1", "").length();
		int num2 = x - rolls.replace("2", "").length();
		int num3 = x - rolls.replace("3", "").length();
		int num4 = x - rolls.replace("4", "").length();
		int num5 = x - rolls.replace("5", "").length();
		int num6 = x - rolls.replace("6", "").length();
		if (num6 == 1) {
			System.out.println(rolls.indexOf('6')/2+1);
		} else if (num5 == 1) {
			System.out.println(rolls.indexOf('5')/2+1);
		} else if (num4 == 1) {
			System.out.println(rolls.indexOf('4')/2+1);
		} else if (num3 == 1) {
			System.out.println(rolls.indexOf('3')/2+1);
		} else if (num2 == 1) {
			System.out.println(rolls.indexOf('2')/2+1);
		} else if (num1 == 1) {
			System.out.println(rolls.indexOf('1')/2+1);
		} else {
			System.out.println("none");
		}
	}
}
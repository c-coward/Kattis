import java.util.*;

public class Datum {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int[] months = {
			0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
		};

		int d = scan.nextInt();
		int m = scan.nextInt();

		int day = d + months[m-1];

		String[] week = {
			"Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"
		};

		System.out.println(week[day % 7]);
	}
}
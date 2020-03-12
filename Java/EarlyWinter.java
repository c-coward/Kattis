import java.util.*;

public class EarlyWinter {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int d = scan.nextInt();
		boolean flag = false;
		int k = 0;

		for (int i = 0; i < n; i++) {
			int di = scan.nextInt();
			if (di <= d) {
				flag = true;
				k = i;
				break;
			}
		}

		if (flag) {
			System.out.println("It hadn't snowed this early in " + k + " years!");
		} else {
			System.out.println("It had never snowed this early!");
		}
	}
}
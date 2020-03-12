import java.util.*;

public class MixedFractions {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		boolean flag = true;

		while (true) {
			int n = scan.nextInt();
			int d = scan.nextInt();

			if(n == 0 && d == 0) {
				break;
			} else {
				int w = n/d;
				int r = n % d;
				System.out.println(w + " " + r + " / " + d);
			}
		}
	}
}
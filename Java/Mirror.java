import java.util.*;

public class Mirror {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();

		for (int i = 1; i < t+1; i++) {
			int r = scan.nextInt();
			int c = scan.nextInt();
			scan.nextLine();
			System.out.println("Test " + i);
			String string = "";
			String out = "";

			for (int l = 0; l < r; l++) {
				string += scan.nextLine() + " ";
			}

			String[] strings = string.split(" ");
			for (int k = r-1; k >= 0; k--) {
				for (int m = c-1; m >= 0; m--) {
					out += (strings[k].charAt(m));
				}
				out += "\n";
			}
			System.out.println(out);
		}
	}
}
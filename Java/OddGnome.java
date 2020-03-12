import java.util.*;

public class OddGnome {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		// System.out.println(n);
		for (int i = 0; i < n; i++) {
			String gnomes = scan.nextLine();
			String[] gnomeSplit = gnomes.split(" ");
			for (int j = 2; j < gnomeSplit.length; j++) {
				int x = Integer.parseInt(gnomeSplit[j]);
				if (x != Integer.parseInt(gnomeSplit[j-1]) + 1) {
					System.out.println(j);
					break;
				}
			}
		}
	}
}
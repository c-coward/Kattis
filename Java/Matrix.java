import java.util.Scanner;

public class Matrix {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		int i = 1;

		while (in.hasNext()) {
			int a = in.nextInt(), b = in.nextInt();
			int c = in.nextInt(), d = in.nextInt();

			int det = a * d - b * c;
		
			System.out.println("Case " + (i++) + ":");
			System.out.println((d / det) + " " + (-b / det));
			System.out.println((-c / det) + " " + (a / det));
		}
	}
}
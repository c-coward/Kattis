import java.util.Scanner;

public class Autori {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String last = " ";
		String string = scan.nextLine();

		String[] array = string.split("-");

		for (int i = 0; i < array.length; i ++) {
			last = last + array[i].charAt(0);
		}

		System.out.println(last);
	}
}
import java.util.Scanner;
import java.util.HashSet;

public class NoDup {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] text = scan.nextLine().split(" ");
		HashSet<String> words = new HashSet<String>();
		boolean repeats = false;
		for (int i = 0; i < text.length; i++) {
			if(words.contains(text[i])) {
				repeats = true;
				break;
			} else {
				words.add(text[i]);
			}
		}
		if(repeats) {
			System.out.println("no");
		} else {
			System.out.println("yes");
		}
	}
}

//n^2 bullshit -v
/*public class NoDup {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String in = scan.nextLine();
		String[] words = in.split(" ");
		int count = 0;
		boolean flag = true;

		for (int i = 0; i < words.length; i ++) {
			for (int l = 0; l < words.length; l ++) {
				if(words[i].equals(words[l])) {
					count += 1;
				}
				if (count > i+1) {
					flag = false;
					break;
				}
			}
			if (count > i+1) {
				break;
			}
		}
		if (flag) {
			System.out.println("yes");
		} else {
			System.out.println("no");
		}
	}
}*/
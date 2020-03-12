import java.util.*;

public class PigLatin {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<String> lines = new ArrayList<String>();
		while(true) {
			try {
				lines.add(scan.nextLine());
			} catch(Exception e) {
				break;
			}
		}

		String[] splitLine;
		for (int i = 0; i < lines.size(); i++) {
			String oneLine = "";
			splitLine = lines.get(i).split(" ");
			for (int l = 0; l < splitLine.length; l++) {
				char x = splitLine[l].charAt(0);
				if (x == 'a' || x == 'e' || x == 'i' ||
					x == 'o' || x == 'u' || x == 'y') {
					oneLine += splitLine[l] + "yay ";
				} else {
					for (int m = 1; m < splitLine[l].length(); m++) {
						char y = splitLine[l].charAt(m);
						if (y == 'a' || y == 'e' || y == 'i' ||
							y == 'o' || y == 'u' || y == 'y') {
							oneLine += splitLine[l].substring(m,splitLine[l].length()) + splitLine[l].substring(0,m) + "ay ";
						break;
						}
					}
				}
			}
			System.out.println(oneLine);
		}
	}
}
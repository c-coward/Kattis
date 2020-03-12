import java.util.*;

public class AddingWords {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		ArrayList<String> words = new ArrayList<String>();
		ArrayList<Integer> nums = new ArrayList<Integer>();
		while (scan.hasNext()) {
			String[] line = scan.nextLine().split(" ");
			String command = line[0];
			if (command.equals("def")) {
				String word = line[1];
				int num = Integer.parseInt(line[2]);
				if (!nums.contains(num)) {
					if (words.contains(word)) {
						words.set(words.indexOf(word), word);
						nums.set(words.indexOf(word), num);
					} else {
						words.add(word);
						nums.add(num);
					}
				}	
			} else if (command.equals("clear")) {
				words.clear();
				nums.clear();
			} else {
				String output = "";
				boolean canDo = true;
				int sum = 0;
				for (int i = 1; i < line.length; i++) {
					try {
						output += line[i] + " ";
						if (i == 1) {
							sum += nums.get(words.indexOf(line[1]));
						} else if (line[i].equals("+")) {
							sum += nums.get(words.indexOf(line[i+1]));
						} else if (line[i].equals("-")) {
							sum -= nums.get(words.indexOf(line[i+1]));
						} else if (line[i].equals("=")) {
							break;
						} else if (!words.contains(line[i])) {
							canDo = false;
						}
					} catch (Exception e) {
						canDo = false;
					}
				}
				if (nums.contains(sum) && canDo) {
					output += words.get(nums.indexOf(sum));
				} else {
					output += "unknown";
				}
				System.out.println(output);
			}
		}
	}
}
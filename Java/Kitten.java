import java.util.*;

public class Kitten {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int k = Integer.parseInt(scan.nextLine());
		HashMap<Integer, Integer> branches = new HashMap<Integer, Integer>();
		String[] line = scan.nextLine().split(" ");

		while(Integer.parseInt(line[0]) != -1) {
			int first = Integer.parseInt(line[0]);
			int[] rest = new int[line.length-1];

			for (int i = 1; i < line.length; i++) {
				rest[i-1] = Integer.parseInt(line[i]);
			}

			for (int x : rest) {
				branches.put(x, first);
			}

			line = scan.nextLine().split(" ");
		}

		String output = "";
		int curr = k;
		while (branches.containsKey(curr)) {
			output += curr + " ";
			curr = branches.get(curr);
		}

		System.out.println(output + curr);
	}
}
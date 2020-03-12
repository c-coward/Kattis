import java.util.*;

public class Flexible {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int width = scan.nextInt();
		int parts = scan.nextInt();

		ArrayList<Integer> partList = new ArrayList<Integer>();
		for (int i = 0; i < parts; i++) {
			partList.add(scan.nextInt());
		}
		partList.add(0);
		partList.add(width);
		TreeSet<Integer> possible = new TreeSet<Integer>();
		for (int i = 0; i < partList.size(); i++) {
			for (int j = i; j < partList.size(); j++) {
				if(j != i) {
					possible.add(Math.abs(partList.get(i) - partList.get(j)));
				}
			}
		}
		String output = "";
		ArrayList<Integer> asList = new ArrayList<Integer>(possible.tailSet(0));
		for (int i = 0; i < asList.size(); i++) {
			output += asList.get(i) + " ";
		}
		System.out.println(output.trim());
	}
}
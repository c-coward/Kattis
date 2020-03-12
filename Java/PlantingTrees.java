import java.util.*;

public class PlantingTrees {
	public static void main(String[] args) {
		TreeMap<Integer, Integer> seeds = new TreeMap<Integer, Integer>();
		Scanner scan = new Scanner(System.in);
		int n = Integer.parseInt(scan.nextLine());
		for (int i = 0; i < n; i++) {
			int x = scan.nextInt();
			if (seeds.containsKey(x)) {
				seeds.put(x, seeds.get(x) + 1);
			} else {
				seeds.put(x, 1);
			}
		}
		// System.out.println(seeds);
		ArrayList<Integer> days = new ArrayList<Integer>(seeds.keySet());
		ArrayList<Integer> times = new ArrayList<Integer>(seeds.values());
		// System.out.println(days);
		// System.out.println(times);
		int timeSum = 1;
		int daySum = 0;
		for (int i = days.size() - 1; i >= 0; i--) {
			int x = days.get(i) + times.get(i) + timeSum;
			if (x > daySum) {
				daySum = x;
			}
			timeSum += times.get(i);
		}
		System.out.println(daySum);
	}
}
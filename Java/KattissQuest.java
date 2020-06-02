import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.TreeMap;

public class KattissQuest {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		TreeMap<Integer, PriorityQueue<Integer>> questList = new TreeMap<>();

		int c = in.nextInt();
		for (int i = 0; i < c; i++) {
			String command = in.next();
			
			if (command.equals("add")) {
				int e = in.nextInt(), g = -in.nextInt();
			
				if (!questList.containsKey(e))
					questList.put(e, new PriorityQueue<Integer>());

				questList.get(e).add(g);
			
			} else {
				int totalEnergy = in.nextInt();
				long totalGold = 0;

				while (totalEnergy > 0) {
					Integer bestCost = questList.floorKey(totalEnergy);

					if (bestCost == null)
						break;

					while (totalEnergy >= bestCost) {
						totalEnergy -= bestCost;
						totalGold -= questList.get(bestCost).poll();

						if (questList.get(bestCost).isEmpty()) {
							questList.remove(bestCost);
							break;
						}
					}
				}

				System.out.println(totalGold);
			}
		}
	}
}
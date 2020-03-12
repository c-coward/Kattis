import java.util.Scanner;
import java.util.HashMap;
import java.util.Stack;
import java.util.PriorityQueue;
import java.util.ArrayList;

public class Detour {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		HashMap<Integer, HashMap<Integer, Integer>> roads =
			new HashMap<Integer, HashMap<Integer, Integer>>();

		int n = in.nextInt();
		int m = in.nextInt();

		for (int i = 0; i < m; i++) {
			int a = in.nextInt();
			int b = in.nextInt();
			int d = in.nextInt();

			if (!roads.containsKey(a)) roads.put(a, new HashMap<Integer, Integer>());
			if (!roads.containsKey(b)) roads.put(b, new HashMap<Integer, Integer>());

			roads.get(a).put(b, d);
			roads.get(b).put(a, d);
		}

		int[] bestPath = new int[n];
		for (int i = 0; i < n; i++) {
			bestPath[i] = -1;
		}

		PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
		pq.add(new Tuple(1,0,-2));

		while (!pq.isEmpty()) {
			Tuple curr = pq.poll();
			
			int i = curr.index;
			int d = curr.dist;
			int p = curr.prev;

			if (bestPath[i] != -1) continue;
			bestPath[i] = p;

			HashMap<Integer, Integer> roadsOut = roads.get(i);
			for (int road : roadsOut.keySet()) {
				if (bestPath[road] != -1) continue;

				pq.add(new Tuple(road, d + roadsOut.get(road), i));
			}
		}

		int[] newPath = new int[n];
		for (int i = 0; i < n; i++) {
			newPath[i] = -1;
		}
		newPath[0] = -2;

		Stack<Tuple> stack = new Stack<Tuple>();
		stack.push(new Tuple(0,0,-2));

		while (!stack.isEmpty()) {
			Tuple curr = stack.pop();

			int i = curr.index;
			int d = curr.dist;
			int p = curr.prev;

			if (i == 1) break;

			HashMap<Integer, Integer> roadsOut = roads.get(i);
			for (int road : roadsOut.keySet()) {
				if (newPath[road] != -1 || bestPath[i] == road) continue;
				newPath[road] = i;
				stack.push(new Tuple(road, d + roadsOut.get(road), i));
			}
		}

		if (newPath[1] == -1) {
			System.out.println("impossible");
		} else {
			ArrayList<Integer> path = new ArrayList<Integer>();
			int curr = 1;

			while (curr != -2) {
				path.add(curr);
				curr = newPath[curr];
			}

			System.out.print(path.size());
			for (int i = path.size() - 1; i >= 0; i--) {
				System.out.print(" " + path.get(i));
			}
			System.out.println();
		}
	}

	static class Tuple implements Comparable<Tuple> {
		int index;
		int dist;
		int prev;

		public Tuple(int index, int dist, int prev) {
			this.index = index;
			this.dist = dist;
			this.prev = prev;
		}

		public int compareTo(Tuple t) {
			return this.dist - t.dist;
		}
	}
}
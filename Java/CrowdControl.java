import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Solution to Kattis's crowdcontrol problem using a priority queue to keep track of
 * the minimum distance of any edge used on a path through the graph from 0 -> n - 1
 * while prioritizing taking edges of maximum weight.
 */
public class CrowdControl {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt(), m = in.nextInt();

		// Streets contain Node -> node, (weight, streetIndex)
		HashMap<Integer, HashMap<Integer, Pair>> streets = new HashMap<>();

		for (int i = 0; i < m; i++) {
			int a = in.nextInt(), b = in.nextInt(), c = in.nextInt();

			if (!streets.containsKey(a))
				streets.put(a, new HashMap<>());
			if (!streets.containsKey(b))
				streets.put(b, new HashMap<>());

			streets.get(a).put(b, new Pair(c, i));
			streets.get(b).put(a, new Pair(c, i));
		}
		
		// Visited points backwards towards the node that a node was reached from
		HashMap<Integer, Integer> visited = new HashMap<>();

		PriorityQueue<Edge> pq = new PriorityQueue<>();
		int minimum = Integer.MAX_VALUE;
		pq.add(new Edge(0, -1, minimum));

		while (!pq.isEmpty()) {
			Edge curr = pq.poll();
			int ind = curr.u, prev = curr.v, min = curr.d;

			if (visited.containsKey(ind))
				continue;
			visited.put(ind, prev);

			if (ind == n - 1) {
				minimum = min;
				break;
			}

			HashMap<Integer, Pair> edges = streets.get(ind);
			for (int next : edges.keySet()) {
				// Never revisit nodes
				if (visited.containsKey(next))
					continue;

				// Keep track of the lowest capacity edge used in any given path
				int nextWeight = edges.get(next).weight;
				int newMin = nextWeight < min ? nextWeight : min;
				pq.add(new Edge(next, ind, newMin));
			}
		}

		boolean[] blockedEdges = new boolean[m];
		int p = n - 1;
		int next = -1;
		while (p != -1) {
			int curr = p;
			int prev = visited.get(p);

			// Look through all nodes used in the path, and block unused edges
			HashMap<Integer, Pair> edges = streets.get(curr);
			for (int nextNode : edges.keySet()) {
				if (nextNode != prev && nextNode != next)
					blockedEdges[edges.get(nextNode).index] = true;
			}

			next = curr;
			p = prev;
		}

		// Print each blocked edge index, or "none" if all edges used
		boolean anyEdgeBlocked = false;
		for (int i = 0; i < m; i++) {
			if (blockedEdges[i]) {
				anyEdgeBlocked = true;
				System.out.print(i + " ");
			}
		}
		System.out.println(anyEdgeBlocked ? "" : "none");
	}

	/**
	 * Class for storing and comparing Edges in the priority queue.
	 */
	static class Edge implements Comparable<Edge> {
		int u;
		int v;
		int d;

		public Edge(int u, int v, int d) {
			this.u = u;
			this.v = v;
			this.d = d;
		}

		/**
		 * Imposes a strictly non-increasing ordering on Edges.
		 */
		public int compareTo(Edge that) {
			return that.d - this.d;
		}
	}

	/**
	 * Class for storing the weight and index of edges.
	 */
	static class Pair {
		int weight, index;

		public Pair(int weight, int index) {
			this.weight = weight;
			this.index = index;
		}
	}
}
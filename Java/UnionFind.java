import java.util.Scanner;

public class UnionFind {
	static int[] parents;
	static int[] rank;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int q = in.nextInt();

		parents = new int[n];
		rank = new int[n];

		for (int i = 0; i < n; i++) {
			parents[i] = i;
			rank[i] = 1;
		}

		for (int i = 0; i < q; i++) {
			String op = in.next();
			int a = in.nextInt();
			int b = in.nextInt();

			if (op.equals("?")) {
				if (find(a) == find(b)) {
					System.out.println("yes");
				} else {
					System.out.println("no");
				}
			} else {
				union(a,b);
			}
		}
		in.close();
	}

	public static int find(int a) {
		if (a == parents[a]) return a;

		parents[a] = find(parents[a]);
		return parents[a];
	}

	public static void union(int a,int b) {
		int parentA = find(a);
		int parentB = find(b);

		if (parentA == parentB) return;

		if (rank[parentA] > rank[parentB]) {
			parents[parentB] = parentA;
		} else if (rank[parentB] > rank[parentA]){
			parents[parentA] = parentB;
		} else {
			parents[parentB] = parentA;
			rank[parentA] += 1;
		}
	}
}
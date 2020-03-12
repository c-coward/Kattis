import java.util.*;

public class Grid {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int m = scan.nextInt();

		int[][] grid = new int[n][m];
		for (int i = 0; i < n; i++) {
			String next = scan.next();
			for (int j = 0; j < m; j++) {
				grid[i][j] = next.charAt(j)-'0';
			}
		}
		boolean flag = false;
		Queue<Integer> queue = new LinkedList<Integer>();
		HashMap<Integer, Integer> distances = new HashMap<Integer, Integer>();
		queue.add(0);
		distances.put(0,0);
		while (!queue.isEmpty()) {
			int curr = queue.poll();
			// validate curr
			if (curr == n*m-1) {
				flag = true;
				break;
			}
			if (curr < 0 || curr > n*m-1) {
				continue;
			}
			int dist = distances.get(curr);
			// System.out.println("curr " + curr);
			// System.out.println("dist " + dist);
			int x = curr/m, y = curr%m;
			int jump = grid[x][y];
			if (x == (curr-jump)/m && !distances.containsKey(curr-jump)) {
				queue.add(curr - jump);
				distances.put(curr-jump, dist + 1);
			} 
			if (x == (curr+jump)/m && !distances.containsKey(curr+jump)) {
				queue.add(curr + jump);
				distances.put(curr+jump, dist + 1);
			}
			if (!distances.containsKey(curr-jump*m)) {
				queue.add(curr - jump*m);
				distances.put(curr-jump*m, dist + 1);
			}
			if (!distances.containsKey(curr+jump*m)) {
				queue.add(curr + jump*m);
				distances.put(curr+jump*m, dist + 1);
			}
		}
		if (flag) {
			System.out.println(distances.get(n*m-1)); 
		} else {
			System.out.println("-1");
		}
	}
}
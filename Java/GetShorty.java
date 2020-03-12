import java.util.*;

public class GetShorty {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		String[] line = scan.nextLine().split(" ");
		String[] endCase = {"0","0"};
		while (!Arrays.equals(line, endCase)) {
			int inter = Integer.parseInt(line[0]);
			int corr = Integer.parseInt(line[1]);
			HashMap<Integer, Double> distances = new HashMap<Integer, Double>();

			ArrayList<HashMap<Integer, Double>> neighbors = new ArrayList<HashMap<Integer, Double>>();
			for (int i = 0; i < inter; i++) {
				neighbors.add(new HashMap<Integer, Double>());
			}

			for (int i = 0; i < corr; i++) {
				String[] edge = scan.nextLine().split(" ");
				int a = Integer.parseInt(edge[0]);
				int b = Integer.parseInt(edge[1]);
				double c = Double.parseDouble(edge[2]);

				HashMap<Integer, Double> temp = neighbors.get(a);
				temp.put(b, c);
				neighbors.set(a, temp);

				temp = neighbors.get(b);
				temp.put(a, c);
				neighbors.set(b, temp);
			}

			PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>(corr, new TupleCompare());

			Tuple start = new Tuple();
			start.index = 0;
			start.size = 1.0;
			pq.add(start);

			while (!pq.isEmpty()) {
				//System.out.println(pq);
				Tuple curr = pq.poll();
				//System.out.println(curr);
				distances.put(curr.index, curr.size);
				if (curr.index == inter-1) {
					break;
				}
				//System.out.println(distances);
				HashMap<Integer, Double> neighb = neighbors.get(curr.index);
				for (int n : neighb.keySet()) {
					if (distances.containsKey(n)) {
						continue;
					}
					Tuple temp = new Tuple();
					temp.index = n;
					temp.size = curr.size*neighb.get(n);
					pq.add(temp);
				}
			}

			System.out.println(String.format("%.4f", distances.get(inter-1)));
			line = scan.nextLine().split(" ");
		}

	}
}

class Tuple {
	int index;
	double size;

	public String toString() {
		String output = "{Index: " + index
			+ " Size: " + size + "}";
		return output;
	}
}

class TupleCompare implements Comparator<Tuple> {
	public int compare(Tuple t1, Tuple t2) {
		if (t1.size < t2.size) {
			return 1;
		} else if (t1.size > t2.size) {
			return -1;
		}
		return 0;
	}
}
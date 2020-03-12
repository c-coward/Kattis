import java.util.*;

public class Throwns {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] temp = scan.nextLine().split(" ");
		int n = Integer.parseInt(temp[0]);
		int c = Integer.parseInt(temp[1]);
		int t = 0;
		String[] throwns = scan.nextLine().split(" ");
		ArrayList<Integer> adds = new ArrayList<Integer>();
		for (int i = 0; i < throwns.length; i++) {
			try {
				int command = Integer.parseInt(throwns[i]);
				adds.add(command);
			} catch(Exception e) {
				int j = adds.size() - 1;
				int back = Integer.parseInt(throwns[i+1]);
				for (int k = 0; k < back; k++) {
					adds.remove(j-k);
				}
				i++;
			}
		}
		for (int i = 0; i < adds.size(); i++) {
			t += adds.get(i);
		}
		int r = t % n;
		if (r < 0) {
			r += n;
		}
		System.out.println(r);
	}
}
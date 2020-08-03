import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class IntegerLists {
	/*
	 * I didn't notice any substantial difference between the two solution methods
	 */
	public static void main(String[] args) {
		//usingDeque();
		usingArray();
	}

	/**
	 * A solution to this problem using a deque two pop off values from each end of the list
	 */
	public static void usingDeque() {
		Scanner in = new Scanner(System.in);

		int tests = in.nextInt();

		for ( ; tests > 0; tests--) {
			String cmds = in.next();
			int listSize = in.nextInt();
			String line = in.next();

			LinkedList<String> list = new LinkedList<>(Arrays.asList(line.substring(1, line.length() - 1).split(",")));
			if (list.getFirst().equals(""))
				list.clear();

			boolean left = true;
			boolean error = false;
			for (int i = 0; i < cmds.length(); i++) {
				char cmd = cmds.charAt(i);

				if (cmd == 'R') {
					left = !left;
				} else {
					if (list.isEmpty()) {
						error = true;
						break;
					}

					if (left)
						list.pollFirst();
					else
						list.pollLast();
				}
			}

			if (error) {
				System.out.println("error");
			} else if (list.isEmpty()) {
				System.out.println("[]");
			} else {
				Iterator<String> it;

				if (left)
					it = list.listIterator();
				else
					it = list.descendingIterator();

				// StringBuilder is used to save on print time
				StringBuilder sb = new StringBuilder();
				
				sb.append("[");

				while (it.hasNext()) {
					sb.append(it.next());
					sb.append(",");
				}
				
				sb.delete(sb.length() - 1, sb.length());
				sb.append("]");

				System.out.println(sb);
			}
		}
	}

	/**
	 * A solution to this problem using an array
	 * Two bounding integers are used in place of the two ends of a deque
	 * These integers set the lower (inclusive) and upper (exclusive) bounds
	 */
	public static void usingArray() {
		Scanner in = new Scanner(System.in);

		int tests = in.nextInt();

		for ( ; tests > 0; tests--) {
			String cmds = in.next();
			int listSize = in.nextInt();
			String line = in.next();

			String[] list = line.substring(1, line.length() - 1).split(",");
			if (list[0].equals(""))
				list = new String[0];

			boolean left = true;
			boolean error = false;
			int l = 0, r = listSize;

			for (int i = 0; i < cmds.length(); i++) {
				char cmd = cmds.charAt(i);

				if (cmd == 'R')
					left = !left;
				else {
					if (l == r) {
						error = true;
						break;
					}

					if (left)
						l++;
					else
						r--;
				}
			}

			if (error)
				System.out.println("error");
			else if (l == r)
				System.out.println("[]");
			else {
				// StringBuilder is used to save on print time
				StringBuilder sb = new StringBuilder();

				if (left) {
					sb.append("[" + list[l]);

					for (int i = l + 1; i < r; i++) {
						sb.append("," + list[i]);
					}

					sb.append("]");
				} else {
					sb.append("[" + list[r - 1]);

					for (int i = r - 2; i >= l; i--) {
						sb.append("," + list[i]);
					}

					sb.append("]");
				}

				System.out.println(sb);
			}
		}
	}
}
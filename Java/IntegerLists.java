import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class IntegerLists {
	public static void main(String[] args) {
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

					if (left) {
						list.pollFirst();
					} else {
						list.pollLast();
					}
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
}
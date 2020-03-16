import java.util.Scanner;
import java.util.Stack;

public class KnightSearch {
	static int length;
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Stack<Tuple> stack = new Stack<Tuple>();
		String search = "ICPCASIASG";

		length = in.nextInt();
		String board = in.next();

		Tuple[] dirs = {
			new Tuple(2,1,1),
			new Tuple(2,-1,1),
			new Tuple(-2,1,1),
			new Tuple(-2,-1,1),
			new Tuple(1,2,1),
			new Tuple(1,-2,1),
			new Tuple(-1,2,1),
			new Tuple(-1,-2,1)
		};

		for (int i = 0; i < length; i++) {
			for (int j = 0; j < length; j++) {
				if (board.charAt(i*length+j) == 'I') stack.push(new Tuple(j,i,0));
			}
		}

		while (!stack.isEmpty()) {
			Tuple curr = stack.pop();
			if (curr.i == 9) {
				System.out.println("YES");
				return;
			}

			for (Tuple d : dirs) {
				Tuple n = curr.add(d);

				if (n.onBoard() && board.charAt(n.y*length+n.x) == search.charAt(n.i)) {
					stack.push(n);
				}
			}
		}

		System.out.println("NO");
	}

	static class Tuple {
		int x;
		int y;
		int i;

		public Tuple(int x, int y, int i) {
			this.x = x;
			this.y = y;
			this.i = i;
		}

		public Tuple add(Tuple t) {
			return new Tuple(this.x + t.x, this.y + t.y, this.i + t.i);
		}

		public boolean onBoard() {
			return (this.x >= 0 && this.x < length
					  && this.y >= 0 && this.y < length);
		}
	}
}
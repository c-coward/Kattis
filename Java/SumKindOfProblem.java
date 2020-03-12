import java.util.*;

public class SumKindOfProblem {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int p = scan.nextInt();
		for (int i = 0; i < p; i ++) {
			int k = scan.nextInt();
			int n = scan.nextInt();
			int s1 = 0;
			int s2 = 0;
			int s3 = 0;
			int num = 1;
			for (int l = 1; l <= n; l ++) {
				s1 += l;
				s2 += 2*l-1;
				s3 += 2*l;
			}

			System.out.println(k + " " + s1 + " " + s2 + " " + s3);
		}	
	}
}
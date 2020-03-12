import java.util.*;
import java.lang.Math;

public class Beehives {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while(true) {
			double d = scan.nextDouble();
			int n = scan.nextInt();
			int sweet = n;
			int sour = 0;
			if(d == 0.0 && n == 0) {
				break;
			}
			Beehive[] hives = new Beehive[n];
			for (int i = 0; i < n; i++) {
				hives[i] = new Beehive(scan.nextDouble(), scan.nextDouble());
			}
			for (int i = 0; i < n-1; i++) {
				for (int j = i + 1; j < n; j++) {
					if (d > hives[i].distance(hives[j])) {
						hives[i].hasFought = true;
						hives[j].hasFought = true;
					}
				}
			}
			for (int i = 0; i < n; i++) {
				if (hives[i].hasFought) {
					sweet--;
					sour++;
				}
			}
			System.out.println(sour + " sour, " + sweet + " sweet");
		}
	}
}

class Beehive {
	public double x;
	public double y;
	public boolean hasFought;

	public Beehive(double a, double b) {
		x = a;
		y = b;
		hasFought = false;
	}

	public double distance(Beehive b) {
		return Math.hypot(b.x - x, b.y - y);
	}
}
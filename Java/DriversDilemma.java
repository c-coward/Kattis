import java.util.*;

public class DriversDilemma {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		float c = scan.nextFloat();
		float x = scan.nextFloat();
		float m = scan.nextFloat();
		boolean canDrive = false;
		int topSpeed = 0;

		for (int i = 0; i < 6; i++) {
			int s = scan.nextInt();
			float e = scan.nextFloat();
			float drive = (float) c/2 - x*m/s - m/e;

			if (drive >= 0.000001) {
				canDrive = true;
				topSpeed = s;
			}
		}
		if (canDrive) {
			System.out.println("YES " + topSpeed);
		} else {
			System.out.println("NO");
		}
	}
}

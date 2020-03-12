import java.util.*;

public class Mjehuric {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String nums = scan.nextLine();
		boolean ordered = false;
		while(!ordered) {
			for (int i = 0; i < nums.length()-2; i += 2) {
				if (nums.equals("1 2 3 4 5")) {
					ordered = true;
					break;
				} else if (Character.getNumericValue(nums.charAt(i)) > Character.getNumericValue(nums.charAt(i+2))) {
					char newS = nums.charAt(i+2);
					char newL = nums.charAt(i);
					nums = nums.substring(0,i) + Character.toString(newS) + " " + Character.toString(newL) + nums.substring(i+3, nums.length());
					System.out.println(nums);
				}
			}
		}
	}
}
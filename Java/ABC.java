import java.util.*;
public class ABC {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] nums = {scan.nextInt(),scan.nextInt(),scan.nextInt()};
		String order = scan.next();
		Arrays.sort(nums);
		String output = "";
		for (int i = 0; i < order.length(); i++) {
			output += (order.charAt(i) == 'A' ? nums[0]
				: order.charAt(i) == 'B' ? nums[1]
				: nums[2]) + " ";
		}
		System.out.println(output);
	}
}
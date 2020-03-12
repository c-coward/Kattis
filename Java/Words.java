import java.util.*;

public class Words {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while (true) {
			try {
				String temp = scan.nextLine();
				String[] arr = temp.split(" ");
				String output = "";
				for (int i = 0; i < arr.length; i++) {
					try {
						int t = Integer.parseInt(arr[i]);
						if (arr[i].length() == 1) {
							output += toNum(t);
						} else if (arr[i].charAt(0) == '1') {
							if (t == 10) {
								output += "ten ";
							} else if (t == 11) {
								output += "eleven ";
							} else if (t == 12) {
								output += "twelve ";
							} else if (t == 13) {
								output += "thirteen ";
							} else if (t == 14) {
								output += "fourteen ";
							}else if (t == 15) {
								output += "fifteen ";
							}else if (t == 16) {
								output += "sixteen ";
							}else if (t == 17) {
								output += "seventeen ";
							}else if (t == 18) {
								output += "eighteen ";
							}else if (t == 19) {
								output += "nineteen ";
							}
						} else {
							if (arr[i].charAt(0) == '2') {
								output += "twenty";
							} else if (arr[i].charAt(0) == '3') {
								output += "thirty";
							} else if (arr[i].charAt(0) == '4') {
								output += "forty";
							} else if (arr[i].charAt(0) == '5') {
								output += "fifty";
							} else if (arr[i].charAt(0) == '6') {
								output += "sixty";
							} else if (arr[i].charAt(0) == '7') {
								output += "seventy";
							} else if (arr[i].charAt(0) == '8') {
								output += "eighty";
							} else if (arr[i].charAt(0) == '9') {
								output += "ninety";
							}
							if (arr[i].charAt(1) != '0') {
								output += "-" + toNum(Integer.parseInt(String.valueOf(arr[i].charAt(1))));
							} else {
								output += " ";
							}
						}
					} catch (NumberFormatException n) {
						output += arr[i] + " ";
					}
				}
				output = Character.toUpperCase(output.charAt(0)) + output.substring(1);
				System.out.println(output);
			} catch (NoSuchElementException e) {
				break;
			}
		}
	}
	public static String toNum(int t) {
		String output = "";
		if (t == 0) {
			output += "zero ";
		} else if (t == 1) {
			output += "one ";
		} else if (t == 2) {
			output += "two ";
		} else if (t == 3) {
			output += "three ";
		} else if (t == 4) {
			output += "four ";
		} else if (t == 5) {
			output += "five ";
		} else if (t == 6) {
			output += "six ";
		} else if (t == 7) {
			output += "seven ";
		} else if (t == 8) {
			output += "eight ";
		} else if (t == 9) {
			output += "nine ";
		}
		return output;
	}
}
import java.util.*;

public class Okvir {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int wordNum = scan.nextInt();
		int letterNum = scan.nextInt();
		int up = scan.nextInt();
		int left = scan.nextInt();
		int right = scan.nextInt();
		int down = scan.nextInt();
		scan.nextLine();

		String words = "";
		for (int i = 0; i < wordNum; i++) {
			words += scan.nextLine() + " ";
		}
		String[] wordList = words.split(" ");

		String output = "";
		for(int i = 0; i < wordNum + up + down; i++) {
			String temp = "";
			for(int l = 0; l < letterNum + left + right; l++) {
				if ((i + l) % 2 == 0) {
					temp += "#";
				} else {
					temp += ".";
				}
			}
			output += temp + " ";
		}

		for (int i = 0; i < wordNum; i++) {
			int leftBias = (up+i)*(left+right+letterNum+1)+left;
			output = output.substring(0,leftBias) + wordList[i]
					+ output.substring(leftBias+letterNum,output.length());
		}

		String[] outputList = output.split(" ");

		for (int i = 0; i < outputList.length; i++) {
			System.out.println(outputList[i]);
		}
	}
}
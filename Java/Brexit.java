import java.util.*;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

public class Brexit {
	public static void main(String[] args) {
		Kattio in = new Kattio(System.in);
		int countries = in.getInt();
		int trades = in.getInt();
		int me = in.getInt() - 1;
		int firstOut = in.getInt() - 1;
		ArrayList<HashSet<Integer>> partners = new ArrayList<HashSet<Integer>>();
		int[] sizes = new int[countries];
		for (int i = 0; i < countries; i++) {
			partners.add(new HashSet<Integer>());
		}

		for (int i = 0; i < trades; i++) {
			int a = in.getInt() - 1;
			int b = in.getInt() - 1;

			partners.get(a).add(b);
			partners.get(b).add(a);
			sizes[a] ++;
			sizes[b] ++;
 		}

 		sizes[firstOut] *= 2;
 		boolean[] left = new boolean[countries];
 		Queue<Integer> q = new LinkedList<Integer>();
 		q.add(firstOut);

 		while (!q.isEmpty()) {
 			int curr = q.poll();
 			if (left[curr]) {
 				continue;
 			}

 			if (partners.get(curr).size() <= sizes[curr]/2) {
 				left[curr] = true;
	 			for (int part : partners.get(curr)) {
	 				if (left[part]) {
	 					continue;
	 				}
 					partners.get(part).remove(curr);
 					q.add(part);
 				}
 			}

 			if (partners.get(me).size() <= sizes[me]/2) {
 				break;
 			}
 		}

 		if (partners.get(me).size() <= sizes[me]/2) {
 			System.out.println("leave");
 		} else {
 			System.out.println("stay");
 		}
	}
}

class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
	super(new BufferedOutputStream(System.out));
	r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
	super(new BufferedOutputStream(o));
	r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
	return peekToken() != null;
    }

    public int getInt() {
	return Integer.parseInt(nextToken());
    }

    public double getDouble() { 
	return Double.parseDouble(nextToken());
    }

    public long getLong() {
	return Long.parseLong(nextToken());
    }

    public String getWord() {
	return nextToken();
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
	if (token == null) 
	    try {
		while (st == null || !st.hasMoreTokens()) {
		    line = r.readLine();
		    if (line == null) return null;
		    st = new StringTokenizer(line);
		}
		token = st.nextToken();
	    } catch (IOException e) { }
	return token;
    }

    private String nextToken() {
	String ans = peekToken();
	token = null;
	return ans;
    }
}
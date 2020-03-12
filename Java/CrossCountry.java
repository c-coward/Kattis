import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

public class CrossCountry {
	public static void main(String[] args) {
		Kattio kio = new Kattio(System.in);

		int n = kio.getInt();
		int s = kio.getInt();
		int t = kio.getInt();

		int[][] graph = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				graph[i][j] = kio.getInt();
			}
		}

		int[] distances = new int[n];
		PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
		Tuple start = new Tuple();
		start.index = s;
		start.dist = 0;
		pq.add(start);

		while (!pq.isEmpty()) {
			Tuple curr = pq.poll();

			distances[curr.index] = curr.dist;

			if (curr.index == t) break;

			for (int i = 0; i < n; i++) {
				if (curr.index == i || distances[i] != 0) continue;

				Tuple temp = new Tuple();
				temp.index = i;
				temp.dist = curr.dist + graph[curr.index][i];
				
				pq.add(temp);
			}
		}

		System.out.println(distances[t]);
	}
}

class Tuple implements Comparable<Tuple> {
	int index;
	int dist;
	public int compareTo(Tuple t) {
		return this.dist - t.dist;
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
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

public class WheresMyInternet {
	static int[] parents;

	public static void main(String[] args) {
		Kattio in = new Kattio(System.in);

		int n = in.getInt();
		int m = in.getInt();

		parents = new int[n];
		for (int i = 0; i < n; i++) {
			parents[i] = i;
		}

		for (int i = 0; i < m; i++) {
			int u = in.getInt() - 1;
			int v = in.getInt() - 1;

			union(u, v);
		}

		boolean connected = true;
		for (int i = 1; i < n; i++) {
			if (find(i) != find(0)) {
				in.println(i + 1);
				connected = false;
			}
		}

		if (connected) {
			in.println("Connected");
		}

		in.close();
	}

	public static void union(int u, int v) {
		int findU = find(u);
		int findV = find(v);

		parents[findU] = findV;
	}

	public static int find(int u) {
		if (parents[u] != u) {
			parents[u] = find(parents[u]);
		}

		return parents[u];
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
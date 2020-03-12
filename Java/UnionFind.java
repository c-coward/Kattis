import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

public class UnionFind {
    static int[] parents;
    static int[] rank;

    public static void main(String[] args) {
        Kattio in = new Kattio(System.in);
        int n = in.getInt();
        int q = in.getInt();

        parents = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parents[i] = i;
            rank[i] = 1;
        }

        for (int i = 0; i < q; i++) {
            String op = in.getWord();
            int a = in.getInt();
            int b = in.getInt();

            if (op.equals("?")) {
                if (find(a) == find(b)) {
                    in.println("yes");
                } else {
                    in.println("no");
                }
            } else {
                union(a,b);
            }
        }
        in.close();
    }

    public static int find(int a) {
        if (a == parents[a]) return a;

        parents[a] = find(parents[a]);
        return parents[a];
    }

    public static void union(int a,int b) {
        int parentA = find(a);
        int parentB = find(b);

        if (parentA == parentB) return;

        if (rank[parentA] > rank[parentB]) {
            parents[parentB] = parentA;
        } else if (rank[parentB] > rank[parentA]){
            parents[parentA] = parentB;
        } else {
            parents[parentB] = parentA;
            rank[parentA] += 1;
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

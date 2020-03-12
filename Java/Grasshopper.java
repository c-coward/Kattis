import java.util.Scanner;
import java.util.LinkedList;

public class Grasshopper {
    private static class Tuple {
        int x, y;
        int d;

        public Tuple(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }

        public Tuple add(Tuple t) {
            return new Tuple(this.x+t.x, this.y+t.y, this.d+t.d);
        }
    }

    public static void main(String[] args) {
        Tuple[] dirs = {
            new Tuple(2,1,1),
            new Tuple(2,-1,1),
            new Tuple(-2,1,1),
            new Tuple(-2,-1,1),
            new Tuple(1,2,1),
            new Tuple(1,-2,1),
            new Tuple(-1,2,1),
            new Tuple(-1,-2,1),
        };

        Scanner in = new Scanner(System.in);

        while (in.hasNext()) {
            int r = in.nextInt();
            int c = in.nextInt();
            int gr = in.nextInt()-1;
            int gc = in.nextInt()-1;
            int lr = in.nextInt()-1;
            int lc = in.nextInt()-1;

            LinkedList<Tuple> q = new LinkedList<Tuple>();
            int[] dists = new int[r*c];
            for (int i = 0; i < r*c; i++) {
                dists[i] = -1;
            }
            
            q.add(new Tuple(gc, gr, 0));
            dists[gr*c+gc] = 0;

            while (!q.isEmpty()) {
                Tuple curr = q.poll();
                int x = curr.x;
                int y = curr.y;
                int d = curr.d;

                if (x == lc && y == lr) {
                    break;
                }
                
                for (Tuple tuple : dirs) {
                    Tuple t = curr.add(tuple);
                    if (t.x < c && t.x >= 0 && t.y < r && t.y >= 0 && dists[t.y*c+t.x] == -1) {
                        dists[t.y*c+t.x] = t.d;
                        q.add(t);
                    }
                }
            }
            int distance = dists[lr*c+lc];
            System.out.println(distance == -1 ? "impossible" : distance);
        }
    }
}

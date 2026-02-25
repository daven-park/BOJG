import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, K;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] in_degree, weight;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for(int t = 1; t <= T; t++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            in_degree = new int[N + 1];
            weight = new int[N + 1];
            graph = new ArrayList<>();
            for (int i = 0; i <= N; i++) graph.add(new ArrayList<>());

            st = new StringTokenizer(br.readLine());
            for(int i = 1; i <= N; i++){
                weight[i] = Integer.parseInt(st.nextToken());
            }

            for(int i = 0; i < K; i++){
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());
                in_degree[Y]++;
                graph.get(X).add(Y);
            }
            int target = Integer.parseInt(br.readLine());
            System.out.println(bfs(target));
        }

    }

    public static int bfs(int target){
        Queue<Integer> q = new LinkedList<>();
        int[] dp = new int[N + 1];
        for(int i = 1; i <= N; i++){
            if(in_degree[i] == 0) {
                q.add(i);
                dp[i] = weight[i];
            }
        }

        while(!q.isEmpty()){
            int current = q.poll();
            if(current == target) return dp[target];
            for(int neighbor : graph.get(current)){
                dp[neighbor] = Math.max(dp[neighbor], dp[current] + weight[neighbor]);
                if(--in_degree[neighbor] != 0) continue;
                q.add(neighbor);
            }
        }
        return dp[target];
    }
}
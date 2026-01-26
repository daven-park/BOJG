import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int N;
    static int[][] board;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        dp = new int[N][N][3];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][1][0] = 1;
        for(int i = 0; i < N; i++){
            for(int j = 2; j < N; j++){
                if (board[i][j] == 1) continue;
                if (j - 1 >= 0){
                    dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2];
                }
                if (i - 1 >= 0){
                    dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2];
                }
                if(i > 0 && j > 0 && board[i - 1][j] == 0 && board[i][j - 1] == 0){
                    dp[i][j][2] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2];
                }
            }
        }

        System.out.println(dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]);
    }
}


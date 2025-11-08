import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int R, C, answer = 0;
    public static char[][] board;
    public static boolean[] used = new boolean[26];
    public static int[] dx = {0, 0, 1, -1};
    public static int[] dy = {1, -1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        board = new char[R][C];
        for(int i = 0; i < R; i++){
            String input = br.readLine();
            for(int j = 0; j < C; j++){
                board[i][j] = input.charAt(j);
            }
        }
        used[board[0][0] - 'A'] = true;
        dfs(0, 0, 1);
        System.out.println(answer);
    }


    public static void dfs(int x, int y, int cnt){
        if (cnt > answer) {
            answer = cnt;
        }
        for(int d = 0; d < 4; d ++){
            int nx = dx[d] + x;
            int ny = dy[d] + y;
            if(nx < 0 || ny < 0 || nx >= R || ny >= C) continue;
            if (used[board[nx][ny] - 'A']) continue;
            used[board[nx][ny] - 'A'] = true;
            dfs(nx, ny, cnt + 1);
            used[board[nx][ny] - 'A'] = false;
        }
    }
}


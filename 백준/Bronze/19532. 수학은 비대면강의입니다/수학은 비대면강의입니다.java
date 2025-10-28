import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int f = Integer.parseInt(st.nextToken());

        int det = a * e - b * d;
        int x, y;

        if (det != 0) {
            x = (c * e - b * f) / det;
            y = (a * f - c * d) / det;
        } else {
            // 안전 폴백(문제 조건상 유일 정수해가 존재)
            x = y = 0;
            outer:
            for (int i = -999; i <= 999; i++) {
                for (int j = -999; j <= 999; j++) {
                    if (a * i + b * j == c && d * i + e * j == f) {
                        x = i; y = j;
                        break outer;
                    }
                }
            }
        }
        System.out.println(x + " " + y);
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.io.*;
import java.util.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    public static HashMap<Character, ArrayList<Integer>> hm = null;
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int tc = 1; tc <= T; tc++){
            String ans = "yes";
            hm = new HashMap<>();

            // 0 ~ 9까지 각 숫자는 등장하지 않거나 등장하면 정확히 2번
            // 숫자d 가 두번 등장하면 그 숫자 사이 개수는 d개
            String target = br.readLine();


            if(!CheckDoubleCount(target)){
                ans = "no";
            }

            if(!CheckNumbersCount()){
                ans = "no";
            }

            System.out.println(ans);
        }

    }

    public static boolean CheckDoubleCount(String target){
        for(int i = 0; i < target.length(); i++){
            char ch = target.charAt(i);
            if(!hm.containsKey(ch)){
                hm.put(ch, new ArrayList<>());
            }
            hm.get(ch).add(i);
        }

        for(Character ch : hm.keySet()){
            if (hm.get(ch).size() != 2){
                return false;
            }
        }
        return true;
    }

    public static boolean CheckNumbersCount(){
        for(Character ch : hm.keySet()){
            if(hm.get(ch).size() != 2) return false;
            if(hm.get(ch).get(1) - hm.get(ch).get(0) - 1 != Character.getNumericValue(ch)){
                return false;
            }
        }

        return true;
    }
}
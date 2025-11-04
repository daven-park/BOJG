import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Stack{
    private final int MAX_STACK_SIZE = 1000001;
    private int length;
    private final int[] array = new int[MAX_STACK_SIZE];

    public Stack(){

    }

    public void push(int number){
        this.array[this.length++] = number;
    }

    public int pop(){
        if (this.isEmpty() == 1) return -1;
        return this.array[--this.length];
    }

    public int size(){
        return this.length;
    }

    public int isEmpty(){
        return this.length == 0 ? 1 : 0;
    }

    public int peek(){
        return this.isEmpty() == 1 ? -1 : this.array[this.length - 1];
    }

}

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        Stack stack = new Stack();
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int operation = Integer.parseInt(st.nextToken());
            if (operation == 1){
                int X = Integer.parseInt(st.nextToken());
                stack.push(X);
            }else if(operation == 2){
                System.out.println(stack.pop());
            }else if(operation == 3){
                System.out.println(stack.size());
            }else if(operation == 4){
                System.out.println(stack.isEmpty());
            }else if(operation == 5){
                System.out.println(stack.peek());
            }
        }
    }
}
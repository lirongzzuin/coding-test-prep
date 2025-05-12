package programmers.level2.fibonacci;

public class Fibonacci {
    public static int solution(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int mod = 1234567;
        int a = 0;
        int b = 1;

        for (int i = 2; i <= n; i++) {
            int temp = (a + b) % mod;
            a = b;
            b = temp;
        }

        return b;
    }

    public static void main(String[] args) {
        System.out.println(solution(3)); // 출력: 2
        System.out.println(solution(5)); // 출력: 5
    }
}
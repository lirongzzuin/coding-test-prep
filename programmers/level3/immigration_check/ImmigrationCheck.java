package programmers.level3.immigration_check;

import java.util.Arrays;

public class ImmigrationCheck {
    public static long solution(int n, int[] times) {
        Arrays.sort(times);
        long start = 1;
        long end = (long) times[times.length - 1] * n;
        long answer = end;

        while (start <= end) {
            long mid = (start + end) / 2;
            long people = 0;

            for (int time : times) {
                people += mid / time;
            }

            if (people >= n) {
                answer = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] times = {7, 10};
        int n = 6;
        System.out.println(solution(n, times));  // 출력: 28
    }
}
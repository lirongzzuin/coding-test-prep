package programmers.level2.target_number;

public class TargetNumber {
    static int count = 0;
    static int target = 0;

    public static int solution(int[] numbers, int targetVal) {
        target = targetVal;
        dfs(numbers, 0, 0);
        return count;
    }

    private static void dfs(int[] numbers, int idx, int sum) {
        if (idx == numbers.length) {
            if (sum == target) {
                count++;
            }
            return;
        }
        dfs(numbers, idx + 1, sum + numbers[idx]);
        dfs(numbers, idx + 1, sum - numbers[idx]);
    }

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(solution(numbers, target));  // 출력: 5
    }
}

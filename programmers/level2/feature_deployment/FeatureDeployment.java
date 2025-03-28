package programmers.level2.feature_deployment;

import java.util.*;

public class FeatureDeployment {
    public static int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> days = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int day = (int) Math.ceil((double) remain / speeds[i]);
            days.offer(day);
        }

        while (!days.isEmpty()) {
            int current = days.poll();
            int count = 1;

            while (!days.isEmpty() && days.peek() <= current) {
                days.poll();
                count++;
            }
            result.add(count);
        }

        return result.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(Arrays.toString(solution(progresses, speeds)));  // [2, 1]
    }
}

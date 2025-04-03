package programmers.level2.custom_sort_string;

import java.util.Arrays;

public class CustomSortString {
    public static String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (s1, s2) -> {
            if (s1.charAt(n) == s2.charAt(n)) {
                return s1.compareTo(s2);
            } else {
                return Character.compare(s1.charAt(n), s2.charAt(n));
            }
        });
        return strings;
    }

    public static void main(String[] args) {
        String[] input = {"sun", "bed", "car"};
        int n = 1;
        System.out.println(Arrays.toString(solution(input, n)));  // ["car", "bed", "sun"]
    }
}
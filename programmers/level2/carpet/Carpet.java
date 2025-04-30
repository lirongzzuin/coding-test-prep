package programmers.level2.carpet;

public class Carpet {
    public static int[] solution(int brown, int yellow) {
        int total = brown + yellow;

        for (int height = 3; height <= total / height; height++) {
            int width = total / height;

            if ((width - 2) * (height - 2) == yellow) {
                return new int[]{width, height};
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int brown = 10, yellow = 2;
        int[] result = solution(brown, yellow);
        System.out.println("[" + result[0] + ", " + result[1] + "]");  // [4, 3]
    }
}


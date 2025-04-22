package programmers.level3.word_transformation;

import java.util.*;

public class WordTransformation {
    static class Node {
        String word;
        int depth;
        Node(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
    }

    public static int solution(String begin, String target, String[] words) {
        Set<String> visited = new HashSet<>();
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(begin, 0));

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            if (current.word.equals(target)) {
                return current.depth;
            }

            for (String next : words) {
                if (!visited.contains(next) && canConvert(current.word, next)) {
                    visited.add(next);
                    queue.add(new Node(next, current.depth + 1));
                }
            }
        }

        return 0;
    }

    private static boolean canConvert(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
            if (count > 1) return false;
        }
        return count == 1;
    }

    public static void main(String[] args) {
        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};
        System.out.println(solution(begin, target, words));  // 출력: 4
    }
}

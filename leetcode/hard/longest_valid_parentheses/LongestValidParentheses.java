package leetcode.hard.longest_valid_parentheses;

import java.util.Stack;

public class LongestValidParentheses {
    public static int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        int maxLen = 0;
        int start = -1;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    start = i;
                } else {
                    stack.pop();
                    if (stack.isEmpty()) {
                        maxLen = Math.max(maxLen, i - start);
                    } else {
                        maxLen = Math.max(maxLen, i - stack.peek());
                    }
                }
            }
        }

        return maxLen;
    }

    public static void main(String[] args) {
        System.out.println(longestValidParentheses("(()"));       // 2
        System.out.println(longestValidParentheses(")()())"));    // 4
        System.out.println(longestValidParentheses(""));          // 0
    }
}

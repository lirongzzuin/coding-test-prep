package baekjoon.silver.printer_queue;

import java.util.*;

public class PrinterQueue {
    static class Document {
        int index;
        int priority;

        Document(int index, int priority) {
            this.index = index;
            this.priority = priority;
        }
    }

    public static int getPrintOrder(int N, int M, int[] priorities) {
        Queue<Document> queue = new LinkedList<>();
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < N; i++) {
            queue.offer(new Document(i, priorities[i]));
            priorityQueue.offer(priorities[i]);
        }

        int count = 0;

        while (!queue.isEmpty()) {
            Document current = queue.poll();

            if (current.priority == priorityQueue.peek()) {
                count++;
                priorityQueue.poll();

                if (current.index == M) {
                    return count;
                }
            } else {
                queue.offer(current);
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        while (T-- > 0) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int[] priorities = new int[N];

            for (int i = 0; i < N; i++) {
                priorities[i] = sc.nextInt();
            }

            System.out.println(getPrintOrder(N, M, priorities));
        }

        sc.close();
    }
}

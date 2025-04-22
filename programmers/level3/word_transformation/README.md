# 단어 변환 (Word Transformation)

## ✅ 문제 설명

주어진 시작 단어 `begin`을 목표 단어 `target`으로 변환하려 합니다.
변환할 때는 다음 규칙을 따릅니다:

- 한 번에 한 글자만 변경할 수 있습니다.
- 변경한 단어는 반드시 주어진 단어 목록 `words` 안에 있어야 합니다.

`begin`에서 `target`으로 변환하는 데 필요한 **최소 변환 단계 수**를 구하세요.

---

## 📥 입력

- `begin` (String): 시작 단어 (길이 3~10)
- `target` (String): 목표 단어 (길이 3~10)
- `words[]` (String[]): 변환 가능한 단어 목록 (1 ≤ words.length ≤ 50)

---

## 📤 출력

- 최소 변환 단계 수 (int)
- 변환할 수 없는 경우 0 반환

---

## 💡 예제

```java
begin = "hit";
target = "cog";
words = ["hot", "dot", "dog", "lot", "log", "cog"];
// 출력: 4
```

(변환 과정: hit → hot → dot → dog → cog)

---

## 🔍 풀이 흐름 및 설명

이 문제는 "가장 짧은 경로"를 찾는 문제입니다.
따라서 **BFS (너비 우선 탐색)** 을 사용해서 해결합니다.

### ✅ 핵심 아이디어

- 현재 단어에서 한 글자만 다른 단어들을 찾아 다음 탐색 대상으로 추가합니다.
- BFS를 사용하면 가장 먼저 도착한 경로가 최단 거리입니다.
- 변환이 완료되면 즉시 탐색을 종료하고 결과를 반환합니다.

---

### 1️⃣ BFS로 한 글자 차이 단어들을 탐색

- 현재 단어와 비교해서 **한 글자만 다른 단어**를 찾아 큐에 추가합니다.
- 이미 방문한 단어는 다시 방문하지 않도록 합니다.

```java
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
```

---

## ⏱ 시간 복잡도 분석

| 연산 항목     | 시간 복잡도 |
|----------------|--------------|
| 전체 탐색      | O(n² * m)    |

- n: words 배열의 크기 (최대 50)
- m: 단어 하나의 길이 (최대 10)

---

## ✅ 전체 코드 (Java)

```java
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
```

---

## ✅ 마무리 정리

- 변환 가능한 모든 경로를 BFS로 탐색해야 최단 변환 과정을 찾을 수 있습니다.
- 한 글자만 다른지 확인하는 서브 메서드 `canConvert`가 핵심입니다.
- BFS를 통해 최단 경로를 찾는 기본 구조를 확실히 이해하고 연습하는 데 좋은 문제입니다.


# 타겟 넘버 (Target Number)

## ✅ 문제 설명

숫자로 이루어진 배열 `numbers`가 주어집니다.
각 숫자에 `+` 또는 `-` 연산을 자유롭게 붙여서, **모든 경우를 탐색하여** 주어진 `target`을 만드는 경우의 수를 구하세요.

---

## 📥 입력

- `numbers` (int[]): 정수 배열 (2 ≤ numbers.length ≤ 20, 각 수 1 이상 50 이하)
- `target` (int): 만들고자 하는 정수 (1 ≤ target ≤ 1000)

---

## 📤 출력

- `target`을 만들 수 있는 경우의 수 (int)

---

## 💡 예제

```java
numbers = [1, 1, 1, 1, 1];
target = 3;
// 출력: 5
```

(설명: 총 5가지 방법으로 3을 만들 수 있습니다)

---

## 🔍 풀이 흐름 및 설명

이 문제는 **모든 가능한 경우의 수**를 탐색해야 하므로, **DFS (깊이 우선 탐색)** 를 사용해서 해결할 수 있습니다.

### ✅ 핵심 아이디어

- 각 숫자에 대해 `+` 또는 `-`를 붙이는 두 가지 선택이 있습니다.
- 이를 인덱스와 누적 합을 함께 재귀 호출하면서 탐색합니다.
- 모든 숫자를 다 사용했을 때 누적합이 `target`과 같으면 경우의 수를 1 증가시킵니다.

---

### 1️⃣ DFS를 통한 경우의 수 탐색

- 인덱스를 하나씩 이동하면서
  - 현재 숫자를 **더한 경우**와 **뺀 경우**를 모두 탐색합니다.

```java
void dfs(int[] numbers, int idx, int sum) {
    if (idx == numbers.length) {
        if (sum == target) {
            count++;
        }
        return;
    }
    dfs(numbers, idx + 1, sum + numbers[idx]);
    dfs(numbers, idx + 1, sum - numbers[idx]);
}
```

---

## ⏱ 시간 복잡도 분석

| 연산 항목     | 시간 복잡도 |
|----------------|--------------|
| 전체 경우 탐색 | O(2ⁿ)         |

- 최대 2²⁰ ≈ 약 100만 회 → 시간 내 충분히 탐색 가능

---

## ✅ 전체 코드 (Java)

```java
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
```

---


## ✅ 마무리 정리

- 이 문제는 단순 구현이 아니라 **모든 경우를 탐색하는 DFS 구조**를 연습하는 데 매우 적합합니다.
- 앞으로 다양한 탐색 문제(조합, 순열 등)에서도 비슷한 DFS 패턴을 응용할 수 있습니다.


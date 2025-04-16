# 입국 심사 (Immigration Check)

## ✅ 문제 설명

입국 심사를 기다리는 n명의 사람이 줄을 서 있습니다.
각 심사관은 심사하는 데 걸리는 시간이 서로 다릅니다.
모든 사람이 심사를 받는 데 걸리는 **최소 시간**을 구하는 프로그램을 작성하세요.

---

## 📥 입력

- `n` (int): 입국 심사를 기다리는 사람 수 (1 ≤ n ≤ 1,000,000,000)
- `times[]` (int[]): 각 심사관이 한 명을 심사하는 데 걸리는 시간 배열 (1 ≤ times.length ≤ 100,000, 각 값 ≤ 1,000,000,000)

---

## 📤 출력

- 모든 사람이 심사를 마치는 데 걸리는 최소 시간 (long)

---

## 💡 예제

```java
n = 6;
times = [7, 10];
// 출력: 28
```

---

## 🔍 풀이 흐름 및 설명

이 문제는 일반적인 순차 계산이 아닌, **이분 탐색(Binary Search)** 을 활용해야 효율적으로 해결할 수 있습니다.
핵심은 사람 수(n)가 아닌 **시간**을 기준으로 탐색한다는 점입니다.

### 1️⃣ 시간의 최소, 최대 범위를 기준으로 이분 탐색 수행

- 최소 시간: 1초
- 최대 시간: 가장 느린 심사관 * n명
- 그 사이에서 가능한 최소 시간을 이분 탐색으로 찾음

### 2️⃣ mid 시간에 n명 이상을 심사할 수 있는지 판단

- 각 심사관이 mid 시간 동안 심사할 수 있는 인원을 계산하여 전체 인원을 합산
- 가능한 경우 더 작은 시간으로 줄이기 (end = mid - 1)
- 부족한 경우 시간을 늘리기 (start = mid + 1)

---

## ⏱ 시간 복잡도

| 연산 항목 | 시간 복잡도 |
|-----------|---------------|
| 이분 탐색 횟수 | O(log(max_time * n)) |
| 각 중간 시간당 인원 계산 | O(k), k = 심사관 수 |

전체 시간 복잡도는 O(k log n) 수준입니다.

---

## ✅ 전체 코드 (Java)

```java
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
```

---

## 📁 폴더 위치 제안

이 문제는 **프로그래머스 Level 3**, **이분 탐색** 알고리즘 유형의 대표 문제입니다.

```
📂 programmers/level3/immigration_check/
├── ImmigrationCheck.java
├── README.md
```

---

## ✅ 마무리 정리

- 이 문제의 핵심은 탐색의 대상이 시간이라는 점입니다.
- 사람 수를 기준으로 순차 탐색하면 시간 초과가 발생할 수 있습니다.
- **시간 범위에서 이분 탐색을 수행하여 최소 시간을 찾는 전략**이 효과적입니다.
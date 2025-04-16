# 🛂 입국 심사 (Immigration Check)

## ✅ 문제 설명

입국 심사를 기다리는 `n`명의 사람이 줄을 서 있다.  
각 심사관이 한 명을 심사하는 데 걸리는 시간은 서로 다르다.  
모든 사람이 심사를 마치는 데 걸리는 **최소 시간**을 구해야 한다.

---

## 📥 입력

- `n` (int): 입국 심사를 받아야 하는 사람 수 (1 ≤ n ≤ 1,000,000,000)
- `times[]` (int[]): 각 심사관이 한 명을 심사하는 데 걸리는 시간 (1 ≤ times.length ≤ 100,000, 각 값 ≤ 1,000,000,000)

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

이 문제는 사람 수 `n`이 최대 10억으로 매우 크기 때문에, 단순히 시뮬레이션으로 풀 경우 시간 초과가 발생한다.  
따라서 **이분 탐색(Binary Search)** 을 활용해서 시간 범위 내에서 최소 시간을 찾아야 한다.

---

### ✅ 핵심 아이디어

사람 수를 기준으로 탐색하지 않고,  
**주어진 시간 안에 몇 명을 심사할 수 있는지**를 계산하여 최소 시간을 찾는다.

즉, **시간(time)** 을 기준으로 이분 탐색을 수행한다.

---

### 1️⃣ 시간의 최소, 최대값 설정

- 최소 시간은 `1`
- 최대 시간은 가장 느린 심사관이 `n`명을 모두 처리하는 경우 → `max(times) * n`
- 이 값을 이분 탐색의 시작과 끝으로 설정한다.

---

### 2️⃣ mid 시간 동안 처리 가능한 인원 계산

- 중간값 `mid` 동안 각 심사관이 몇 명을 처리할 수 있는지 계산한다.
- 처리 가능한 사람 수의 총합이 `n`보다 크거나 같으면, 해당 시간 안에 모든 사람을 심사할 수 있다.
- 이 경우 더 짧은 시간도 가능한지 보기 위해 `end`를 줄인다.
- 반면 부족한 경우 `start`를 늘린다.

```java
long mid = (start + end) / 2;
long people = 0;
for (int time : times) {
    people += mid / time;
}
```

---

### 3️⃣ 최소 시간 갱신 및 탐색 범위 조정

- `people >= n`이면 `answer = mid`, `end = mid - 1`
- `people < n`이면 `start = mid + 1`

---

## ⏱ 시간 복잡도 분석

| 연산 항목               | 시간 복잡도           |
|------------------------|------------------------|
| 이분 탐색 반복 횟수    | O(log(max_time * n))   |
| 한 번의 인원 계산       | O(k), k = 심사관 수     |

총 시간 복잡도: **O(k log n)**

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

## ✅ 마무리 정리

핵심은 **사람 수가 아닌 시간**을 기준으로 탐색을 수행하는 것이다.  
각 시간마다 몇 명을 처리할 수 있는지를 계산하고, 가능한 최소 시간을 찾아야 한다.  
이런 방식은 **최소값을 빠르게 찾는 문제**에서 자주 쓰이며, 코딩테스트에서도 자주 출제된다.
# 피보나치 수 (Fibonacci Number)

## ✅ 문제 설명

피보나치 수는 다음과 같이 정의된다:

* F(0) = 0
* F(1) = 1
* F(n) = F(n-1) + F(n-2) (n ≥ 2)

정수 `n`이 주어졌을 때, F(n)을 **1234567으로 나눈 나머지**를 반환한다.

---

## 📥 입력

* `n` (int): 2 이상 100,000 이하의 자연수

---

## 📤 출력

* `F(n) % 1234567`

---

## 💡 예제

```java
n = 3; // 출력: 2
n = 5; // 출력: 5
```

---

## 🔍 풀이 흐름 및 설명

이 문제는 대표적인 **동적 계획법(DP, Dynamic Programming)** 문제다.
단순 재귀 방식으로 풀면 같은 계산을 반복하게 되어 시간 초과가 발생하므로,
**반복문 기반의 DP 방식**으로 계산해야 한다.

---

### ✅ 접근 방법

피보나치 수는 이전 두 항을 이용해 다음 항을 만들어내는 점화식을 가진다:
→ `F(n) = F(n-1) + F(n-2)`

`F(0)`부터 `F(n)`까지 순차적으로 계산하여 `F(n)`을 구하면 되고,
중간 결과가 커질 수 있으므로 **계산 과정에서 매번 1234567로 나눈 나머지를 저장**해야 한다.

---

### ✅ 풀이 방식 1: 배열 사용 (Bottom-Up)

```java
long[] dp = new long[n + 1];
dp[0] = 0;
dp[1] = 1;

for (int i = 2; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
}

return dp[n];
```

* 배열 `dp`에 결과를 저장해가며 반복문으로 계산한다.
* 이전 두 값을 이용해 현재 값을 만들어낸다.
* 각 항 계산 시마다 나머지 연산을 수행한다.

➡️ 이해하기 쉬우나 메모리를 더 많이 사용한다.

---

### ✅ 풀이 방식 2: 변수만 사용 (공간 최적화)

```java
int a = 0, b = 1;

for (int i = 2; i <= n; i++) {
    int temp = (a + b) % 1234567;
    a = b;
    b = temp;
}

return b;
```

* 변수 `a`, `b` 두 개만 사용하여 반복적으로 최신 피보나치 값을 갱신한다.
* 배열을 사용하지 않아 공간 효율이 매우 높다.
* 매번 모듈러 연산을 통해 값의 크기를 제한한다.

➡️ 입력 크기가 클 때 유리하다.

---

## ⏱ 시간 및 공간 복잡도 분석

| 항목          | 복잡도  |
| ----------- | ---- |
| 시간 복잡도      | O(n) |
| 공간 복잡도 (배열) | O(n) |
| 공간 복잡도 (변수) | O(1) |

반복문 기반이기 때문에 입력값 `n`에 비례하여 시간이 소요된다.
변수만 사용하는 방법은 공간 사용량을 최소화할 수 있다.

---

## ✅ 전체 코드 (Java)

```java
public class Fibonacci {
    public static int solution(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int mod = 1234567;
        int a = 0;
        int b = 1;

        for (int i = 2; i <= n; i++) {
            int temp = (a + b) % mod;
            a = b;
            b = temp;
        }

        return b;
    }

    public static void main(String[] args) {
        System.out.println(solution(3)); // 출력: 2
        System.out.println(solution(5)); // 출력: 5
    }
}
```

---

## ✅ 마무리 정리

* 피보나치 수열은 대표적인 점화식 기반 DP 문제다.
* 재귀로 풀면 시간 초과가 발생하므로 반드시 반복문 기반으로 해결해야 한다.
* 배열 사용 방식과 변수 사용 방식 두 가지 모두 익혀두면 좋다.
* 이 문제를 통해 **DP의 핵심 개념인 "이전 결과의 재활용"** 원리를 정확히 이해할 수 있다.
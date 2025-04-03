# 큰 수 만들기 (Make the Largest Number)

## ✅ 문제 설명

숫자로 이루어진 문자열 `number`가 주어진다.  
여기에서 **k개의 숫자를 제거**해서 만들 수 있는 가장 큰 수를 문자열 형태로 반환하세요.

---

## 형식

- `number`: 길이 2 이상 1,000,000 이하의 숫자 문자열  
- `k`: 제거할 숫자의 개수 (1 ≤ k < number.length)

---

## 결과

- 가장 큰 수 문자열

---

## 예제

```java
number = "1924", k = 2;       // 출력: "94"
number = "4177252841", k = 4; // 출력: "775841"
```

---

## 풀이 환경 및 설명

이 문제는 "앞에서부터 탐산하며 가장 큰 수를 만들기 위한 조건" 결정을 계속 해야 합니다.  
**스택을 활용한 그리디 알고리즘**으로 다음과 같은 환경으로 해결합니다:

---

### 1️⃣ 앞자리부터 큰 수가 오른 정도로 유지하며 제거

- **이렇게 한 이유?**  
  앞자리 숫자가 작고 뒤에 더 큰 숫자가 있다면, 앞자리를 제거하는 것이 항상 더 큰 수를 만들어줌
- 스택에 숫자를 하나씩 추가하며, 현재 숫자가 스택의 top보다 크고 k가 남아있다면 pop

```java
for (char digit : number.toCharArray()) {
    while (!stack.isEmpty() && k > 0 && stack.peek() < digit) {
        stack.pop();
        k--;
    }
    stack.push(digit);
}
```

---

### 2️⃣ 남은 k가 있다면 뒤에서부터 제거

- 스택에 남은 k개만큼 자리에서 제거해줌
- (처음부터 내배순이었는 경우)

---

### 3️⃣ 최종 결과 반환

- 스택을 문자열로 변환해서 결과 생성

---

## 시간 보캼도

| 연산 | 시간 보캼도 |
|------|--------------|
| 전체 탐산 | O(n) |

※ n은 `number.length()`

---

## 해당 문제의 전체 코드 (Java)

```java
import java.util.Stack;

public class MakeBigNumber {
    public static String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();

        for (char digit : number.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peek() < digit) {
                stack.pop();
                k--;
            }
            stack.push(digit);
        }

        while (k-- > 0) {
            stack.pop();
        }

        StringBuilder sb = new StringBuilder();
        for (char c : stack) sb.append(c);

        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(solution("1924", 2));         // 94
        System.out.println(solution("4177252841", 4));   // 775841
    }
}
```
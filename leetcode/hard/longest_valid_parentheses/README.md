# Longest Valid Parentheses

## ✅ 문제 설명

괄호로 이루어진 문자열 `s`가 주어집니다. 
이 문자열에서 올바른 괄호 쌍으로 이루어진 **가장 긴 연속 부분 문자열의 길이**를 구하세요.

예를 들어 `(()`는 `()`만 유효하므로 길이는 2이고, `)()())`에서는 `()()`가 유효하여 길이는 4입니다.

---

## 📥 입력

- `s`: 괄호로만 구성된 문자열. 길이는 최대 10⁵입니다.
- 문자열은 `'('` 와 `')'` 문자만 포함됩니다.

---

## 📤 출력

- 유효한 괄호 부분 문자열 중 **가장 긴 길이 (정수)**

---

## 💡 예제

```java
s = "(()"       // 출력: 2
s = ")()())"    // 출력: 4
s = ""          // 출력: 0
```

---

## 🔍 풀이 흐름 및 설명

이 문제는 괄호의 유효성을 검사하는 것에서 더 나아가, **가장 긴 유효한 괄호의 길이**를 구해야 합니다. 
이를 위해 스택을 활용한 방법이 가장 효율적이고 직관적입니다.

---

### 1️⃣ 스택에 인덱스를 저장하며 유효한 구간 계산

- **왜 인덱스를 저장하는가?**  
  괄호의 유효성뿐 아니라 "길이"를 구해야 하므로, 인덱스를 이용해 거리 계산이 필요합니다.

- 여는 괄호 `'('`는 스택에 현재 인덱스를 저장합니다.
- 닫는 괄호 `')'`가 등장했을 때:
  - 스택이 비어있으면 현재 인덱스를 시작 기준으로 갱신
  - 비어있지 않다면 스택에서 pop 하고 길이를 계산하여 최대값 갱신

```java
Stack<Integer> stack = new Stack<>();
int maxLen = 0;
int start = -1; // 유효한 시작 위치 초기화

for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    if (c == '(') {
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
```

- 위 로직을 통해, 문자열을 한 번 순회하면서 유효한 괄호 쌍의 최대 길이를 구할 수 있습니다.

---

## ⏱ 시간 복잡도

| 연산 항목     | 시간 복잡도 |
|----------------|--------------|
| 전체 문자열 순회 | O(n)         |

- n은 문자열의 길이입니다. 
- 스택 연산도 전체적으로 O(n)입니다.

---

## ✅ 전체 코드 (Java)

```java
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
```
---

## ✅ 마무리 정리

- 이 문제는 단순 괄호 짝 맞춤이 아닌, **길이 계산**이 핵심입니다.
- 스택에는 괄호 문자가 아닌 **인덱스**를 저장하여 거리 계산을 가능하게 해야 합니다.
- 괄호 유효성 검사의 고급 버전으로, 코딩테스트에서 자주 출제되는 유형입니다.


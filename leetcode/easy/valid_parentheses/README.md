# 올바른 괄호 (Valid Parentheses)

## 문제 설명
괄호로 이루어진 문자열이 주어졌을 때, **괄호의 짝이 모두 맞는지** 확인하는 문제입니다.  
괄호 종류는 다음과 같습니다:
- 여는 괄호: `(`, `{`, `[`  
- 닫는 괄호: `)`, `}`, `]`  

올바른 괄호 문자열이면 `true`, 아니면 `false`를 반환하세요.

## 입력
- `String s`: 괄호로만 구성된 문자열 (1 ≤ s.length ≤ 10⁴)

## 출력
- `true` or `false` (올바른 괄호 문자열 여부)

## 예제
```java
isValid("()")       → true
isValid("()[]{}")   → true
isValid("(]")       → false
```

## 해결 방법
### 1️⃣ 스택(Stack) 활용 - O(n)
- 여는 괄호는 스택에 push
- 닫는 괄호가 나오면 스택의 top과 비교 → 짝이 맞으면 pop
- 처리 후 스택이 비어 있으면 올바른 괄호 문자열

```java
public static boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
        if (c == '(' || c == '{' || c == '[') {
            stack.push(c);
        } else {
            if (stack.isEmpty()) return false;
            char top = stack.pop();
            if ((c == ')' && top != '(') ||
                (c == '}' && top != '{') ||
                (c == ']' && top != '[')) {
                return false;
            }
        }
    }
    return stack.isEmpty();
}
```

## 시간 복잡도 분석
| 연산 | 시간 복잡도 | 공간 복잡도 |
|------|--------------|--------------|
| 전체 처리 | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 짝이 맞는 괄호 쌍 출력하기
- [ ] 문자열 중 가장 깊은 중첩 깊이 구하기
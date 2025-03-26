# 균형잡힌 괄호 문자열 (Balanced Parentheses Check)

## 문제 설명
주어진 문자열 `s`가 **올바른 괄호 문자열인지 확인**하는 프로그램을 작성하세요.  
괄호는 `()`, `{}`, `[]` 세 가지 종류가 있으며, 다음 조건을 만족해야 합니다.
1. 여는 괄호는 반드시 닫는 괄호와 짝이 맞아야 한다.  
2. 닫는 괄호가 여는 괄호보다 먼저 나오면 안 된다.

## 입력
- `s`: 길이 `n` (1 ≤ `n` ≤ 100,000) 의 문자열  
- 괄호 `()`, `{}`, `[]`로만 이루어짐  

## 출력
- 문자열이 올바른 괄호 문자열이면 `true`, 아니면 `false` 반환  

## 예제
```java
isBalanced("(){}[]");  // true
isBalanced("({[)]}");  // false
```

## 해결 방법
### 1️⃣ 스택(Stack) 활용 - O(n)
- 여는 괄호는 스택에 **push**
- 닫는 괄호가 나오면 스택의 **top**과 비교 후 **짝이 맞으면 pop**
- 최종적으로 스택이 비어 있으면 `true`, 그렇지 않으면 `false`

```java
import java.util.Stack;

public class BalancedParentheses {
    public static boolean isBalanced(String s) {
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
}
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 스택 활용 | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] **큐(Queue) 활용 방법 추가**
- [ ] **여는 괄호와 닫는 괄호 개수가 다른 경우 예외 처리**


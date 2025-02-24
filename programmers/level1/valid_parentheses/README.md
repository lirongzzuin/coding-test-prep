# 괄호 유효성 검사 (Valid Parentheses)

## 문제 설명
주어진 문자열 `s`가 **"(", ")", "{", "}", "[", "]"** 로만 이루어져 있을 때,  
괄호의 짝이 올바르게 맞는지 검사하는 함수를 작성하세요.

## 입력
- `s`: 길이 `n` (1 ≤ `n` ≤ 10⁴) 의 문자열 (괄호 문자로만 구성)

## 출력
- 올바른 괄호이면 `True`, 그렇지 않으면 `False` 반환

## 예제
```python
is_valid("()")       # 출력: True
is_valid("()[]{}")   # 출력: True
is_valid("(]")       # 출력: False
is_valid("([)]")     # 출력: False
is_valid("{[]}")     # 출력: True
```

## 해결 방법
### 1️⃣ 스택(Stack) 활용 - O(n)
- 문자열을 순회하며 **여는 괄호**를 스택에 `push`
- **닫는 괄호**를 만나면 스택의 `top`과 비교 후 `pop`
- 올바른 짝이 아니거나 스택이 비어있으면 `False` 반환
- 마지막에 **스택이 비어 있으면 `True`, 그렇지 않으면 `False`**

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # 여는 괄호인 경우
            stack.append(char)
        elif char in mapping.keys():  # 닫는 괄호인 경우
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return not stack  # 스택이 비어있으면 True, 아니면 False
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 스택 활용 | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 입력 검증 추가 (예: 빈 문자열 예외 처리)
- [ ] 여러 유형의 괄호가 섞인 경우 테스트 케이스 보완


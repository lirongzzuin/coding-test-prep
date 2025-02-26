# 회문 판별 (Valid Palindrome)

## 문제 설명
주어진 문자열 `s`가 **대소문자를 구분하지 않고**, **영문자와 숫자만 고려했을 때** 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별하는 함수를 작성하세요.

## 입력
- `s`: 길이 `n` (0 ≤ `n` ≤ 2 * 10⁵) 의 문자열  
- 공백, 특수문자가 포함될 수 있음  
- 대소문자를 구분하지 않음  

## 출력
- 주어진 문자열이 **회문이면 `True`, 아니면 `False`** 반환  

## 예제
```python
is_palindrome("A man, a plan, a canal: Panama")  # 출력: True
is_palindrome("race a car")  # 출력: False
is_palindrome(" ")  # 출력: True
```

## 해결 방법
### 1️⃣ 투 포인터 활용 (Two Pointers) - O(n)
- 문자열을 **알파벳과 숫자로만 정제**한 후, **양 끝에서 비교**
- `left` 포인터와 `right` 포인터를 사용하여 같은지 비교

```python
import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 투 포인터 활용 | **O(n)** | O(1) |

## 추가할 내용
- [ ] 빈 문자열 입력 처리 테스트 케이스 추가
- [ ] 더 다양한 특수문자가 포함된 경우 테스트


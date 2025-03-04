# 숫자의 조합으로 가능한 최대 수 (Largest Number from Digits)

## 문제 설명
정수 배열 `nums`가 주어졌을 때, 배열의 모든 숫자를 조합하여 만들 수 있는 **가장 큰 수**를 문자열 형태로 반환하는 함수를 작성하세요.

## 입력
- `nums`: 길이 `n` (1 ≤ `n` ≤ 100,000) 의 정수 배열  
- 각 원소는 `0 ≤ nums[i] ≤ 10⁹`

## 출력
- `nums`의 숫자들을 조합하여 만들 수 있는 **가장 큰 수**를 문자열 형태로 반환

## 예제
```python
largest_number([10, 2])  # 출력: "210"
largest_number([3, 30, 34, 5, 9])  # 출력: "9534330"
largest_number([0, 0])  # 출력: "0"
```

## 해결 방법
### 1️⃣ 커스텀 정렬 사용 - O(n log n)
- 두 숫자 `a`와 `b`가 있을 때:
  - `a + b`와 `b + a`를 비교하여 더 큰 순서로 정렬
  - 예: `"9" + "34"` vs `"34" + "9"` → `"934"`가 `"349"`보다 크므로 `"9"`가 앞에 와야 함

```python
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1  # a가 앞에 와야 함
    else:
        return 1  # b가 앞에 와야 함

def largest_number(nums):
    nums = list(map(str, nums))  # 숫자를 문자열로 변환
    nums.sort(key=cmp_to_key(compare))  # 커스텀 정렬 적용
    result = ''.join(nums)
    
    return "0" if result[0] == "0" else result  # "000" 방지
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 커스텀 정렬 사용 | **O(n log n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 숫자가 모두 0인 경우 예외 처리
- [ ] 입력 배열이 비어있는 경우 테스트


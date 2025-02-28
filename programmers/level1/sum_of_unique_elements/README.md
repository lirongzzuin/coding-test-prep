# 배열의 고유한 요소 합 (Sum of Unique Elements)

## 문제 설명
정수 배열 `nums`가 주어졌을 때, 배열에서 **한 번만 등장하는 모든 요소의 합**을 구하는 함수를 작성하세요.

## 입력
- `nums`: 길이 `n` (1 ≤ `n` ≤ 100) 의 정수 배열  
- 각 정수의 범위는 `1 ≤ nums[i] ≤ 100`

## 출력
- 배열에서 **한 번만 등장하는 요소들의 합**을 반환

## 예제
```python
sum_of_unique([1, 2, 3, 2])  # 출력: 4  (1 + 3)
sum_of_unique([4, 4, 4, 4])  # 출력: 0  (고유한 숫자 없음)
sum_of_unique([10, 6, 9, 6, 9, 10, 8])  # 출력: 8
```

## 해결 방법
### 1️⃣ 해시맵(딕셔너리) 활용 - O(n)
- 숫자의 등장 횟수를 **딕셔너리**에 저장
- 한 번만 등장하는 숫자들의 합을 계산

```python
from collections import Counter

def sum_of_unique(nums):
    count = Counter(nums)  # 숫자의 등장 횟수 저장
    return sum(num for num, freq in count.items() if freq == 1)
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 해시맵(딕셔너리) | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 빈 배열 입력 처리
- [ ] 더 다양한 테스트 케이스 추가


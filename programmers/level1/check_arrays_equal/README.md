# 두 개의 배열이 동일한 요소를 갖는지 검사 (Check If Two Arrays Are Equal)

## 문제 설명
두 개의 정수 배열 `arr1`과 `arr2`가 주어졌을 때,  
두 배열이 같은 요소를 같은 개수만큼 포함하고 있다면 `True`,  
그렇지 않다면 `False`를 반환하는 함수를 작성하세요.  
배열의 요소 순서는 고려하지 않습니다.

## 입력
- `arr1`, `arr2`: 길이 `n` (1 ≤ `n` ≤ 10⁵) 의 정수 배열  
- 각 배열의 요소는 `-10⁶ ≤ arr[i] ≤ 10⁶` 범위의 정수  

## 출력
- 두 배열이 같은 요소를 같은 개수만큼 포함하면 `True`, 그렇지 않으면 `False` 반환  

## 예제
```python
are_arrays_equal([1, 2, 3, 4], [4, 3, 2, 1])  # 출력: True
are_arrays_equal([1, 2, 3, 4], [1, 2, 2, 3])  # 출력: False
are_arrays_equal([7, 8, 9], [7, 8, 9, 9])     # 출력: False
```

## 해결 방법
### 1️⃣ 해시맵(딕셔너리) 활용 - O(n)
- 각 배열의 요소 개수를 **딕셔너리**에 저장한 후 비교
- `Counter(arr1) == Counter(arr2)` 비교

```python
from collections import Counter

def are_arrays_equal(arr1, arr2):
    return Counter(arr1) == Counter(arr2)
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 해시맵(딕셔너리) | **O(n)** | O(n) |

## 추가할 수 있는 내용
- [ ] 빈 배열 입력 처리
- [ ] 배열의 크기가 다른 경우 테스트


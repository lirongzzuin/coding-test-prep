# 배열에서 두 번째로 큰 값 찾기 (Find Second Largest Number)

## 문제 설명
정수 배열 `nums`가 주어졌을 때, **두 번째로 큰 숫자**를 찾아 반환하는 함수를 작성하세요.  
만약 배열에 두 번째로 큰 숫자가 없다면 `None`을 반환하세요.

## 입력
- `nums`: 길이 `n` (2 ≤ `n` ≤ 10⁶) 의 정수 배열  
- 각 원소는 `-10⁶ ≤ nums[i] ≤ 10⁶` 범위  

## 출력
- 배열에서 **두 번째로 큰 값**을 반환  
- 두 번째로 큰 값이 존재하지 않으면 `None` 반환  

## 예제
```python
find_second_largest([3, 1, 4, 1, 5, 9, 2, 6, 5])  # 출력: 6
find_second_largest([10, 10, 10])  # 출력: None
find_second_largest([7, 3])  # 출력: 3
```

## 해결 방법
### 1️⃣ 두 개의 변수 사용 - O(n)
- 가장 큰 숫자 `first`와 두 번째로 큰 숫자 `second`를 추적  
- 배열을 한 번만 순회하여 두 번째로 큰 값을 찾음  

```python
def find_second_largest(nums):
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 두 개의 변수 사용 | **O(n)** | O(1) |

## 추가할 수 있는 내용
- [ ] 배열의 길이가 2보다 작은 경우 예외 처리
- [ ] 중복 요소가 포함된 경우 추가 테스트


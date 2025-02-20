# 배열에서 두 수의 합 찾기 (Two Sum)

## 문제 설명
정수 배열 `nums`와 목표 정수 `target`이 주어집니다.  
배열에서 두 숫자의 합이 `target`이 되는 인덱스를 찾아 반환하는 함수를 작성하세요.  
(같은 요소를 두 번 사용할 수 없으며, 유일한 해만 존재한다고 가정합니다.)

## 입력
- `nums`: 길이 `n` (2 ≤ `n` ≤ 10⁵) 의 정수 배열 (-10⁹ ≤ `nums[i]` ≤ 10⁹)
- `target`: 정수 (-10⁹ ≤ `target` ≤ 10⁹)

## 출력
- 합이 `target`이 되는 두 숫자의 **인덱스를 담은 리스트** 반환

## 예제
```python
two_sum([2, 7, 11, 15], 9)  # 출력: [0, 1]
two_sum([3, 2, 4], 6)  # 출력: [1, 2]
two_sum([3, 3], 6)  # 출력: [0, 1]
```

## 해결 방법
### 1️⃣ 해시맵 (딕셔너리) 사용 - O(n)
- 요소를 탐색하면서 `target - 현재 요소`가 해시맵에 있는지 확인
- 빠르게 값을 찾을 수 있음 (최적의 방법)

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

### 2️⃣ 브루트포스 (비효율적) - O(n²)
- 모든 숫자 쌍을 탐색하여 합이 `target`이 되는지 확인

```python
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 해시맵 | **O(n)** | O(n) |
| 브루트포스 | O(n²) | O(1) |

## 추가할 수 있는 내용
- [ ] 입력 검증 추가 (예: 빈 배열 예외 처리)
- [ ] 여러 개의 해가 존재할 경우 처리
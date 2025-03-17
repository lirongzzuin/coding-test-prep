# 가장 긴 증가하는 부분 수열 (Longest Increasing Subsequence, LIS)

## 문제 설명
수열 `nums`이 주어졌을 때, **가장 긴 증가하는 부분 수열(LIS)의 길이**를 구하는 프로그램을 작성하세요.

## 입력
- `nums`: 길이 `n` (1 ≤ `n` ≤ 1,000) 의 정수 배열  
- 각 원소는 `1 ≤ nums[i] ≤ 1,000`  

## 출력
- `nums`에서 가장 긴 증가하는 부분 수열(LIS)의 길이 출력  

## 예제
```python
longest_increasing_subsequence([10, 20, 10, 30, 20, 50])  
# 출력: 4  # (10 → 20 → 30 → 50)
```

## 해결 방법
### 1️⃣ 다이나믹 프로그래밍 (DP) 활용 - O(n²)
- `dp[i]`: `nums[i]`를 마지막 원소로 가지는 가장 긴 증가하는 부분 수열의 길이  
- `dp[i] = max(dp[j] + 1)`, 단 `nums[j] < nums[i]` (0 ≤ `j` < `i`)  

```python
def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n  # 모든 원소를 개별적인 LIS로 초기화
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:  # 증가하는 부분 수열 조건
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)  # 가장 긴 증가하는 부분 수열의 길이 반환
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 다이나믹 프로그래밍 (DP) | **O(n²)** | O(n) |

## 추가할 수 있는 내용
- [ ] `O(n log n)` 풀이(이분 탐색 활용) 추가
- [ ] 부분 수열을 실제로 출력하는 코드 구현


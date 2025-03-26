# 가장 긴 증가하는 부분 수열 2 (Longest Increasing Subsequence 2, LIS 2)

## 문제 설명
수열 `nums`이 주어졌을 때, **가장 긴 증가하는 부분 수열(LIS)의 길이**를 구하는 프로그램을 작성하세요.  
이전에 풀었던 **O(n²) DP 풀이**보다 **더 효율적인 O(n log n) 이분 탐색 풀이**를 사용해야 합니다.

## 입력
- `nums`: 길이 `n` (1 ≤ `n` ≤ 1,000,000) 의 정수 배열  
- 각 원소는 `1 ≤ nums[i] ≤ 1,000,000,000`  

## 출력
- `nums`에서 가장 긴 증가하는 부분 수열(LIS)의 길이 출력  

## 예제
```python
longest_increasing_subsequence_2([10, 20, 10, 30, 20, 50])
# 출력: 4  # (10 → 20 → 30 → 50)
```

## 해결 방법
### 1️⃣ 이분 탐색 (Binary Search) + 그리디 활용 - O(n log n)
- 증가하는 부분 수열을 유지하는 리스트 `sub`를 사용  
- `bisect_left(sub, num)`을 이용해 **현재 숫자가 들어갈 위치를 찾음**  
- 기존 값 교체(더 작은 값으로 유지) or 새로운 값 추가  

```python
import bisect

def longest_increasing_subsequence_2(nums):
    sub = []
    
    for num in nums:
        pos = bisect.bisect_left(sub, num)  # num이 들어갈 위치 찾기
        if pos == len(sub):
            sub.append(num)  # 새로운 증가하는 부분 수열 요소 추가
        else:
            sub[pos] = num  # 기존 값 교체 (더 작은 값 유지)
    
    return len(sub)  # LIS 길이 반환
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 이분 탐색 + 그리디 | **O(n log n)** | O(n) |

## 추가할 수 있는 내용
- [ ] LIS의 실제 부분 수열 출력 기능 추가
- [ ] DP O(n²) 풀이와 비교하여 성능 테스트


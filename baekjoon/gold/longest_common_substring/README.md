# 가장 긴 공통 부분 문자열 (Longest Common Substring)

## 문제 설명
두 개의 문자열 `s1`과 `s2`가 주어졌을 때, **두 문자열에 공통으로 포함된 가장 긴 연속된 부분 문자열**의 길이를 구하는 프로그램을 작성하세요.

## 입력
- `s1`, `s2`: 길이 `n, m` (1 ≤ `n, m` ≤ 1,000) 의 영문 소문자로 이루어진 문자열  

## 출력
- 두 문자열에서 가장 긴 공통 부분 문자열의 길이 출력  

## 예제
```python
longest_common_substring("abcdxyz", "xyzabcd")  
# 출력: 4  # "abcd"
```

## 해결 방법
### 1️⃣ 다이나믹 프로그래밍 (DP) 활용 - O(n * m)
- `dp[i][j]`: `s1[0:i]`와 `s2[0:j]`에서 **공통 부분 문자열의 최대 길이**  
- `s1[i-1] == s2[j-1]`이면 `dp[i][j] = dp[i-1][j-1] + 1`  

```python
def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:  # 문자가 같을 경우
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 다이나믹 프로그래밍 (DP) | **O(n * m)** | O(n * m) |

## 추가할 수 있는 내용
- [ ] `O(n log m)` 풀이(이분 탐색 + 해싱) 추가
- [ ] 실제 공통 부분 문자열을 출력하는 코드 구현


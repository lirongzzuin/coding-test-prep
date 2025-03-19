# 가장 긴 팰린드롬 부분 문자열 (Longest Palindromic Substring, LPS)

## 문제 설명
문자열 `s`가 주어졌을 때, **가장 긴 팰린드롬 부분 문자열**을 찾아 반환하는 프로그램을 작성하세요.  
팰린드롬이란 앞에서 읽어도 뒤에서 읽어도 동일한 문자열을 의미합니다.

## 입력
- `s`: 길이 `n` (1 ≤ `n` ≤ 1,000) 의 영문 소문자로 이루어진 문자열  

## 출력
- `s`에서 가장 긴 팰린드롬 부분 문자열 반환  

## 예제
```python
longest_palindromic_substring("babad")  
# 출력: "bab"  # 또는 "aba" (둘 다 정답)
```

## 해결 방법
### 1️⃣ 다이나믹 프로그래밍 (DP) 활용 - O(n²)
- `dp[i][j]`: `s[i:j+1]`이 팰린드롬인지 여부  
- `s[i] == s[j]`이고, `dp[i+1][j-1]`이 `True`면 `dp[i][j]`도 `True`  

```python
def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1
    
    for i in range(n):
        dp[i][i] = True  # 길이 1인 문자열은 항상 팰린드롬
    
    for length in range(2, n + 1):  # 부분 문자열 길이
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if length > max_length:
                    start, max_length = i, length
    
    return s[start:start + max_length]
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 다이나믹 프로그래밍 (DP) | **O(n²)** | O(n²) |

## 추가할 수 있는 내용
- [ ] `O(n)` 풀이(Manacher's Algorithm) 추가
- [ ] 팰린드롬을 확장하는 중심 확장(Center Expansion) 방식 구현


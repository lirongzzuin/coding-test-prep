def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    start, max_length = 0, 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                dp[i][j] = True
                if length > max_length:
                    start, max_length = i, length

    return s[start:start + max_length]

# 테스트 실행
if __name__ == "__main__":
    print(longest_palindromic_substring("babad"))  # "bab" 또는 "aba"
    print(longest_palindromic_substring("cbbd"))  # "bb"
    print(longest_palindromic_substring("a"))  # "a"

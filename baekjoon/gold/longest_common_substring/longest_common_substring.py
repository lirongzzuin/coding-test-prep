def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_length = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

# 테스트 실행
if __name__ == "__main__":
    print(longest_common_substring("abcdxyz", "xyzabcd"))  # 4
    print(longest_common_substring("abcde", "ace"))  # 1
    print(longest_common_substring("abcdef", "ghijkl"))  # 0

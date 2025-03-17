def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n 

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# 테스트 실행
if __name__ == "__main__":
    print(longest_increasing_subsequence([10, 20, 10, 30, 20, 50]))  # 4

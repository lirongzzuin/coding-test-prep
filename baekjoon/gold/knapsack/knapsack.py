import sys

def knapsack(N, W, items):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        weight, value = items[i-1]
        for w in range(W + 1):
            if w >= weight:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N][W]

# 입력 처리
if __name__ == "__main__":
    N, W = map(int, sys.stdin.readline().split())
    items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    print(knapsack(N, W, items))

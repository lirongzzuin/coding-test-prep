def find_largest_square(board):
    n, m = len(board), len(board[0])
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side ** 2 

# 테스트 실행
if __name__ == "__main__":
    print(find_largest_square([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))  # 9
    print(find_largest_square([[0, 0, 1, 1], [1, 1, 1, 1]]))  # 4

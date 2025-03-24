from collections import deque
import sys

def bfs_tomatoes(grid, N, M):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j))

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))

    max_day = 0
    for row in grid:
        for cell in row:
            if cell == 0:
                return -1
            max_day = max(max_day, cell)

    return max_day - 1

# 입력 처리
if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(bfs_tomatoes(grid, N, M))

# 토마토 (Tomato) - BFS 탐색

## 문제 설명
상자 안의 토마토들이 **익어가는 과정**을 시뮬레이션합니다.  
익은 토마토는 **상하좌우에 있는 익지 않은 토마토를 하루 후 익게 만들 수 있습니다.**  
모든 토마토가 익는 데 걸리는 **최소 날짜**를 출력하세요.  
단, 처음부터 모두 익어 있다면 0을 출력하고, 모두 익을 수 없다면 -1을 출력합니다.

## 입력
- 첫째 줄: 상자의 가로 `M`, 세로 `N` (2 ≤ M, N ≤ 1,000)  
- 둘째 줄부터 N개의 줄: 토마토 정보 (`1`: 익음, `0`: 안 익음, `-1`: 없음)

## 출력
- 모든 토마토가 익는 데 걸리는 **최소 일수** 출력  
- 불가능할 경우 `-1` 출력

## 예제 입력
```
6 4
0 0 -1 0 0 0
0 0 1 0 -1 0
0 0 -1 0 0 0
0 0 0 0 -1 1
```

## 예제 출력
```
4
```

## 해결 방법
### 1️⃣ 다중 시작점 BFS - O(N×M)
- 익은 토마토(1)를 **큐에 모두 담고 동시에 BFS 시작**  
- **상하좌우**로 퍼지며 1씩 증가시켜 **익은 날짜를 기록**  
- BFS 종료 후 **가장 큰 날짜 - 1**이 정답

```python
from collections import deque

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
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|--------------|-------------|
| BFS | **O(N × M)** | O(N × M) |

## 추가할 수 있는 내용
- [ ] 3차원 확장 (예: 토마토가 여러 층에 있을 경우)
- [ ] 익은 날짜를 시각화하거나 순차적으로 출력하는 기능 추가


# 가장 큰 정사각형 찾기 (Find Largest Square in a Grid)

## 문제 설명
`n x m` 크기의 이진 행렬(grid)이 주어질 때, `1`로 이루어진 가장 큰 **정사각형의 넓이**를 구하는 함수를 작성하세요.

## 입력
- `board`: `n x m` 크기의 2차원 리스트 (1 ≤ `n, m` ≤ 1,000)  
- 각 원소는 `0` 또는 `1`로만 이루어짐  

## 출력
- `1`로 이루어진 가장 큰 정사각형의 넓이 반환  

## 예제
```python
find_largest_square([[0, 1, 1, 1],  
                     [1, 1, 1, 1],  
                     [1, 1, 1, 1],  
                     [0, 0, 1, 0]])  # 출력: 9 (3x3)

find_largest_square([[0, 0, 1, 1],  
                     [1, 1, 1, 1]])  # 출력: 4 (2x2)
```

## 해결 방법
### 1️⃣ 다이나믹 프로그래밍 (DP) 활용 - O(nm)
- `dp[i][j]`를 `(i, j)` 위치에서 만들 수 있는 **가장 큰 정사각형 한 변의 길이**로 정의  
- `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` (단, `board[i][j] == 1`일 때)  
- 최댓값을 찾고 넓이 계산 (`max_side_length^2`)  

```python
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
    
    return max_side ** 2  # 넓이 반환
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 다이나믹 프로그래밍 | **O(nm)** | O(nm) |

## 추가할 수 있는 내용
- [ ] 행렬에 `1`이 없는 경우 예외 처리
- [ ] 공간 최적화를 위한 1차원 DP 배열 활용
# 용량 제한이 있는 배낭 문제 (Knapsack Problem, 0-1 Knapsack)

## 문제 설명
여러 개의 물건이 주어졌을 때, 각 물건은 **무게(weight)** 와 **가치(value)** 를 가집니다.  
최대 `W` 무게까지 넣을 수 있는 배낭이 있을 때, **가치의 합이 최대가 되도록 물건을 선택하는 프로그램**을 작성하세요.  
각 물건은 **한 번만** 선택할 수 있습니다.

## 입력
- 첫째 줄에 `N` (1 ≤ `N` ≤ 100) (물건의 개수)와 `W` (1 ≤ `W` ≤ 10,000) (배낭의 최대 무게)  
- 둘째 줄부터 `N`개의 줄에 각 물건의 `weight`와 `value` (`1 ≤ weight, value ≤ 1,000`)  

## 출력
- 배낭에 넣을 수 있는 물건들의 최대 가치 출력  

## 예제
### **입력**  
```
4 7
6 13
4 8
3 6
5 12
```
### **출력**  
```
14
```

## 해결 방법
### 1️⃣ 다이나믹 프로그래밍 (DP) 활용 - O(N * W)
- `dp[i][w]`: `i`번째 물건까지 고려했을 때, 무게 `w`를 초과하지 않는 최대 가치  
- `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)`  

```python
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
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 다이나믹 프로그래밍 (DP) | **O(N * W)** | O(N * W) |

## 추가할 수 있는 내용
- [ ] **공간 최적화** (1차원 DP 배열 사용) 구현
- [ ] **다른 접근법** (Branch & Bound, Meet-in-the-Middle) 분석


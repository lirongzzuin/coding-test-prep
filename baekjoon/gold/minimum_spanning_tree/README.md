# 최소 스패닝 트리 (Minimum Spanning Tree, MST)

## 문제 설명
그래프가 주어졌을 때, **모든 노드를 포함하면서 간선 가중치 합이 최소가 되는 트리**를 찾는 프로그램을 작성하세요.  
이 트리를 **최소 스패닝 트리(MST)** 라고 합니다.

## 입력
- 첫째 줄: 정점의 개수 `V` (1 ≤ `V` ≤ 100,000)와 간선의 개수 `E` (1 ≤ `E` ≤ 200,000)  
- 둘째 줄부터 `E`개의 줄: `A B C` (정점 `A`와 `B`를 연결하는 가중치 `C`인 간선)

## 출력
- 최소 스패닝 트리(MST)의 가중치 합 출력  

## 예제 입력
```
3 3
1 2 1
2 3 2
1 3 3
```

## 예제 출력
```
3
```

## 해결 방법
### 1️⃣ 크루스칼 알고리즘 (Kruskal’s Algorithm) - O(E log E)
- **간선의 가중치를 기준으로 오름차순 정렬**  
- **유니온 파인드(Disjoint Set Union, DSU) 알고리즘**을 이용하여 사이클을 방지  
- MST에 포함되는 간선이 `V-1`개가 될 때까지 반복

```python
import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 크루스칼 알고리즘 | **O(E log E)** | O(V) |

## 추가할 수 있는 내용
- [ ] 프림 알고리즘(O(E log V))과 비교 분석
- [ ] 입력이 최대일 때 성능 테스트


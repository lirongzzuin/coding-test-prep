import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
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

def kruskal(V, edges):
    parent = list(range(V + 1))
    rank = [0] * (V + 1)
    
    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    edge_count = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_weight += weight
            edge_count += 1
            if edge_count == V - 1:
                break

    return mst_weight

# 입력 처리
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    V, E = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:]]
    
    print(kruskal(V, edges))

import sys
import heapq

def min_meeting_rooms(intervals):
    intervals.sort() 
    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap) 
        heapq.heappush(heap, end) 

    return len(heap)

# 입력 처리
if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    intervals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    print(min_meeting_rooms(intervals))

import sys
import bisect

def longest_increasing_subsequence_2(nums):
    sub = []

    for num in nums:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num) 
        else:
            sub[pos] = num

    return len(sub)

# 입력 처리
if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    print(longest_increasing_subsequence_2(data))

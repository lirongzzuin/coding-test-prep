from collections import Counter

def sum_of_unique(nums):
    count = Counter(nums)
    return sum(num for num, freq in count.items() if freq == 1)

# 테스트 실행
if __name__ == "__main__":
    print(sum_of_unique([1, 2, 3, 2])) 
    print(sum_of_unique([4, 4, 4, 4])) 
    print(sum_of_unique([10, 6, 9, 6, 9, 10, 8])) 

from itertools import combinations

def sum_two_numbers(numbers):
    result = set(sum(pair) for pair in combinations(numbers, 2))
    return sorted(result)

# 테스트 코드
if __name__ == "__main__":
    print(sum_two_numbers([2, 1, 3, 4, 1])) 
    print(sum_two_numbers([5, 0, 2, 7])) 

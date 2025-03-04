def find_second_largest(nums):
    first = second = float('-inf')

    for num in nums:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

# 테스트 실행
if __name__ == "__main__":
    print(find_second_largest([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # 6
    print(find_second_largest([10, 10, 10]))  # none
    print(find_second_largest([7, 3]))  # 3

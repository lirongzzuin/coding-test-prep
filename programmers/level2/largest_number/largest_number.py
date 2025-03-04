from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1 
    else:
        return 1 

def largest_number(nums):
    nums = list(map(str, nums)) 
    nums.sort(key=cmp_to_key(compare))  
    result = ''.join(nums)

    return "0" if result[0] == "0" else result

# 테스트 실행
if __name__ == "__main__":
    print(largest_number([10, 2]))  # "210"
    print(largest_number([3, 30, 34, 5, 9]))  # "9534330"
    print(largest_number([0, 0]))  # "0"
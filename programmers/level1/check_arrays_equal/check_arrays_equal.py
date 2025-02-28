from collections import Counter

def are_arrays_equal(arr1, arr2):
    return Counter(arr1) == Counter(arr2)

# 테스트 실행
if __name__ == "__main__":
    print(are_arrays_equal([1, 2, 3, 4], [4, 3, 2, 1]))  
    print(are_arrays_equal([1, 2, 3, 4], [1, 2, 2, 3]))  
    print(are_arrays_equal([7, 8, 9], [7, 8, 9, 9]))  

def find_kth_number(array, commands):
    result = []
    for i, j, k in commands:
        result.append(sorted(array[i-1:j])[k-1])
    return result

# 테스트 실행
if __name__ == "__main__":
    print(find_kth_number([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  
    # 출력: [5, 6, 3]

def find_min_max(s):
    numbers = list(map(int, s.split()))
    return f"{min(numbers)} {max(numbers)}"

# 테스트 실행
if __name__ == "__main__":
    print(find_min_max("1 2 3 4"))  # "1 4"
    print(find_min_max("-1 -2 -3 -4"))  # "-4 -1"
    print(find_min_max("-1 -1 0 1 1"))  # "-1 1"

def count_number_expressions(n):
    count = 0
    start, end, sum_ = 1, 1, 1

    while start <= n:
        if sum_ < n:
            end += 1
            sum_ += end
        elif sum_ > n:
            sum_ -= start
            start += 1
        else:
            count += 1
            sum_ -= start
            start += 1

    return count

# 테스트 실행
if __name__ == "__main__":
    print(count_number_expressions(15))  # 4
    print(count_number_expressions(10))  # 2
    print(count_number_expressions(1))  # 1
def binary_transform(s):
    count, zero_count = 0, 0

    while s != "1":
        zero_count += s.count("0")
        s = bin(len(s.replace("0", "")))[2:] 
        count += 1

    return [count, zero_count]

# 테스트 실행
if __name__ == "__main__":
    print(binary_transform("110010101001"))  # [3, 8]
    print(binary_transform("01110"))  # [3, 3]
    print(binary_transform("1111111"))  # [0, 0]
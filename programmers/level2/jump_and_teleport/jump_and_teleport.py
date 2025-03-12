def min_energy_to_zero(N):
    energy = 0
    while N > 0:
        if N % 2 == 1:
            energy += 1
        N //= 2 
    return energy

# 테스트 실행
if __name__ == "__main__":
    print(min_energy_to_zero(5))  # 2
    print(min_energy_to_zero(6))  # 2
    print(min_energy_to_zero(5000))  # 5

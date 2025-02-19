# 📌 최소공배수 (LCM) 구하기

## 📖 문제 설명
두 개의 정수 `a`와 `b`가 주어졌을 때, 두 수의 **최소공배수 (LCM, Least Common Multiple)** 를 구하는 함수를 작성하세요.

## 🔢 입력
- `a`, `b`: 1 이상 1,000,000 이하의 정수

## 🎯 출력
- `a`와 `b`의 최소공배수를 반환합니다.

## 💡 예제
```python
lcm(6, 8)  # 출력: 24
lcm(12, 18)  # 출력: 36
```

## 🛠️ 해결 방법
최소공배수는 **두 수의 곱을 최대공약수(GCD)로 나눈 값**

\[
\text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}
\]

Python의 `math` 라이브러리를 활용하면 GCD를 쉽게 구할 수 있다.

## 💻 코드 구현
```python
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# 테스트 실행
if __name__ == "__main__":
    print(lcm(6, 8))  # 24
    print(lcm(12, 18))  # 36
```

## ⏱️ 시간 복잡도
- **O(log(min(a, b)))**: 유클리드 알고리즘을 활용한 GCD 계산이 매우 효율적이므로, 전체 연산도 빠르게 수행된다.
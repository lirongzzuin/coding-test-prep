# 숫자의 표현 (Number Representation)

## 문제 설명
자연수 `n`이 주어졌을 때, 연속된 자연수들의 합으로 `n`을 표현하는 방법의 개수를 구하는 함수를 작성하세요.

예를 들어, `15`는 다음과 같이 4가지 방법으로 표현할 수 있습니다.  
- `1 + 2 + 3 + 4 + 5`
- `4 + 5 + 6`
- `7 + 8`
- `15` (자기 자신)

## 입력
- `n`: 1 ≤ `n` ≤ 10,000

## 출력
- 연속된 자연수의 합으로 `n`을 표현할 수 있는 방법의 개수

## 예제
```python
count_number_expressions(15)  # 출력: 4
count_number_expressions(10)  # 출력: 2
count_number_expressions(1)  # 출력: 1
```

## 해결 방법
### 1️⃣ 투 포인터 (Two Pointers) 활용 - O(n)
- 두 개의 포인터 `start`와 `end`를 사용하여 연속된 숫자의 합을 확인  
- 합이 `n`보다 작으면 `end`를 증가시키고, 크면 `start`를 증가  
- `n`과 같을 경우 카운트 증가  

```python
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
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 투 포인터 사용 | **O(n)** | O(1) |

## 추가할 수 있는 내용
- [ ] `n`이 1인 경우의 처리
- [ ] 성능 최적화를 위한 수학적 접근 방식 검토


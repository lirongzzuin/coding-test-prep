# 두 개 뽑아서 더하기 (Sum Two Numbers)

## 문제 설명
정수 배열 `numbers`가 주어질 때, 서로 다른 두 개의 수를 뽑아 더한 값들을 **오름차순으로 정렬**하여 반환하는 함수를 작성하시오.

## 제한 조건
- `numbers`는 길이가 **2 이상 100 이하**인 리스트이다.
- `numbers`의 원소는 **1 이상 100 이하의 자연수**이다.
- 같은 숫자의 조합이라도 결과값은 중복되지 않는다.

## 입출력 예시
| numbers          | 결과                  |
|----------------|----------------|
| [2, 1, 3, 4, 1] | [2, 3, 4, 5, 6, 7] |
| [5, 0, 2, 7]   | [2, 5, 7, 9, 12]  |

---

## 해결 방법
1. `itertools.combinations(numbers, 2)`를 사용하여 **모든 두 숫자 조합을 생성**한다.
2. 각 조합의 합을 **`set()`을 이용해 중복을 제거**하면서 저장한다.
3. 결과를 **`sorted()`를 사용하여 오름차순으로 정렬**하여 반환한다.

## 코드 구현
```python
from itertools import combinations

def sum_two_numbers(numbers):
    # 두 개의 수를 뽑아 더한 값들의 집합 생성 (중복 제거)
    result = set(sum(pair) for pair in combinations(numbers, 2))
    # 결과를 리스트로 변환 후 오름차순 정렬
    return sorted(result)

# 테스트 코드
if __name__ == "__main__":
    print(sum_two_numbers([2, 1, 3, 4, 1]))  # [2, 3, 4, 5, 6, 7]
    print(sum_two_numbers([5, 0, 2, 7]))    # [2, 5, 7, 9, 12]

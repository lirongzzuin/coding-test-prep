# 가장 긴 공통 접두사 (Longest Common Prefix)

## 문제 설명
문자열 배열 `strs`가 주어졌을 때, 모든 문자열에서 **공통적으로 등장하는 가장 긴 접두사(prefix)** 를 찾아 반환하는 함수를 작성하세요.  
만약 공통 접두사가 없다면 `""` (빈 문자열)를 반환하세요.

## 입력
- `strs`: 길이 `n` (1 ≤ `n` ≤ 200) 의 문자열 리스트
- 각 문자열의 길이는 최대 200이며, 알파벳 소문자로만 구성

## 출력
- 가장 긴 공통 접두사를 반환

## 예제
```python
longest_common_prefix(["flower", "flow", "flight"])  # 출력: "fl"
longest_common_prefix(["dog", "racecar", "car"])    # 출력: ""
longest_common_prefix(["interspecies", "interstellar", "interstate"])  # 출력: "inters"
```

## 해결 방법
### 1️⃣ 정렬 후 첫 번째와 마지막 문자열 비교 - O(n log n)
1. 입력 리스트를 **정렬**
2. 정렬된 배열의 **첫 번째 문자열**과 **마지막 문자열**을 비교하면서 공통 부분을 찾음
3. 가장 짧은 공통 접두사를 반환

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]
```

## 시간 복잡도 분석
| 방법 | 시간 복잡도 | 공간 복잡도 |
|------|----------|----------|
| 정렬 후 비교 | **O(n log n) + O(m)** | O(1) |

## 추가할 수 있는 내용
- [ ] 빈 리스트 입력 처리
- [ ] 성능 최적화를 위한 다른 방법 고려 (예: 분할 정복)


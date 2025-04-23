## 🧬 187. Repeated DNA Sequences (LeetCode)

### 📌 문제 개요

DNA 문자열이 주어졌을 때, **길이가 정확히 10인 부분 문자열(substring)** 중에서 **두 번 이상 등장하는 모든 문자열**을 찾아 리스트로 반환하는 문제다.

DNA는 네 개의 문자 'A', 'C', 'G', 'T'로만 구성되어 있으며, 중복된 10글자 서열만 찾아야 한다.

---

### 📥 입력 조건
- 문자열 `s` (1 <= s.length <= 10^5)
- `s[i]`는 'A', 'C', 'G', 'T' 중 하나

### 📤 출력 조건
- 길이 10인 중복된 문자열들을 리스트 형태로 반환 (순서는 상관없음)

---

### 💡 예제

#### 예제 1
```
입력: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
출력: ["AAAAACCCCC", "CCCCCAAAAA"]
```

#### 예제 2
```
입력: s = "AAAAAAAAAAAAA"
출력: ["AAAAAAAAAA"]
```

---

### 🧠 문제 풀이 흐름

#### 🔹 핵심 아이디어
- 문자열 `s`에서 길이 10인 부분 문자열을 슬라이딩 윈도우로 탐색한다.
- 이미 본 서열을 집합(set)에 저장하며,
- **두 번째 등장한 문자열만 결과 리스트에 추가**한다.

#### 🔹 풀이 흐름
1. 문자열 길이가 10 미만이면 빈 리스트 반환
2. 윈도우를 하나씩 이동하며 `s[i:i+10]` 부분 문자열을 생성
3. 한 번 나온 문자열은 `seen` 집합에 저장
4. 이미 `seen`에 있으면서 `output`에는 없는 문자열이면 `output`에 추가

---

### 💻 풀이 코드 (Python)

```python
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seen = set()
        output = set()

        for i in range(len(s) - 9):  # 길이 10짜리 윈도우
            sub = s[i:i+10]
            if sub in seen:
                output.add(sub)
            else:
                seen.add(sub)

        return list(output)
```

---

### ✏️ 마무리 정리

이 문제는 문자열 슬라이딩 윈도우와 해시셋을 활용한 **중복 탐색의 전형적인 문제**다.

- 중복 확인은 set으로 빠르게 처리할 수 있으며,
- 전체 탐색은 O(n)으로 매우 효율적이다.

파이썬의 집합(set) 자료형을 잘 활용하면 코드가 간결하고 빠르게 동작한다.

---

### ✅ 기억해둘 포인트
- 문자열 길이가 10 미만이면 바로 종료 조건 처리
- 슬라이딩 윈도우의 시작 인덱스는 `range(len(s) - 9)`로 지정
- 중복된 문자열을 찾을 때는 `set` 2개 (`seen`, `output`)를 사용하는 것이 깔끔하고 안전함

## 📚 단어 정렬 (BOJ 1181)

### 📌 문제 개요

N개의 단어가 주어졌을 때, 아래 조건에 따라 정렬된 결과를 출력하는 문제다.

정렬 조건:
1. 길이가 짧은 단어가 먼저
2. 길이가 같으면 사전 순으로 정렬
3. 중복된 단어는 제거

---

### 📥 입력 조건
- 첫째 줄: 단어 개수 N (1 ≤ N ≤ 20,000)
- 다음 N줄: 알파벳 소문자로 구성된 단어 (최대 길이: 50)

### 📤 출력 조건
- 조건에 따라 정렬된 단어들을 한 줄에 하나씩 출력

---

### 💡 예제

#### 입력
```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```

#### 출력
```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```

---

### 🧠 문제 풀이 흐름

#### 🔹 핵심 아이디어
- 먼저 중복 제거를 위해 **set()**을 사용한다
- 정렬 기준은 다음과 같이 튜플로 설정:
  - `sorted(word_set, key=lambda x: (len(x), x))`
    - 첫 번째 기준: 길이 (짧은 순)
    - 두 번째 기준: 사전순 (기본 문자열 정렬)

#### 🔹 흐름 정리
1. 입력 단어를 전부 읽고 set으로 중복 제거
2. 길이와 사전순 기준으로 정렬
3. 정렬된 결과를 출력

---

### 💻 풀이 코드 (Python)

```python
n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
```

---

### ✏️ 마무리 정리

이 문제는 문자열 정렬의 기본 개념과 함께 **여러 정렬 기준을 동시에 적용하는 법**을 연습할 수 있는 문제다.

- 중복 제거: `set()` 활용
- 복합 정렬 기준: `key=lambda x: (기준1, 기준2)` 형태로 적용

파이썬의 정렬 방식은 안정 정렬이며, `sorted()`나 `list.sort()`는 복수 기준을 튜플로 제공할 수 있어 매우 강력하다.

---

### ✅ 기억해둘 포인트
- 문자열 정렬 기준은 기본적으로 **사전순 정렬**
- 여러 기준 정렬 시 튜플 정렬 사용 → `key=lambda x: (기준1, 기준2)`
- 중복 제거는 반드시 `set()` 사용 후 정렬 처리

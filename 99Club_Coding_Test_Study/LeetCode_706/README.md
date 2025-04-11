## 🧩 706. Design HashMap (LeetCode)

### 📌 문제 개요

내장 해시 테이블을 사용하지 않고, 직접 HashMap을 구현하는 문제다.

구현해야 할 기능은 다음과 같다:

- `put(key, value)`: 키-값 쌍을 삽입하거나, 기존 키가 있으면 값을 갱신한다.
- `get(key)`: 키에 해당하는 값을 반환하고, 없으면 `-1` 반환
- `remove(key)`: 키가 존재하면 해당 키와 값을 삭제한다.

---

### 📥 입력 조건
- `0 <= key, value <= 10^6`
- 최대 10^4번의 `put`, `get`, `remove` 연산이 주어진다

### 📤 출력 조건
- 연산별 결과를 리스트 형태로 출력

---

### 💡 예제

#### 입력
```
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
```

#### 출력
```
[null, null, null, 1, -1, null, 1, null, -1]
```

---

### 🧠 문제 풀이 흐름

이 문제는 기본적인 해시 구조에 대한 이해를 바탕으로 직접 해시 충돌을 해결하며 구현해야 한다.

#### 🔹 구조 설계
- 해시 충돌을 방지하기 위해 **배열 + 체이닝(Linked List)** 방식 사용
- 고정된 크기의 버킷 배열 생성 (ex. 크기: 1000)
- 키를 해시 함수로 버킷 인덱스로 변환한 뒤, 해당 버킷에 (key, value) 저장

#### 🔹 주요 연산 흐름
- **put(key, value)**: 해당 버킷에 key가 존재하면 value 갱신, 없으면 삽입
- **get(key)**: 해당 버킷에서 key 탐색 후 존재 여부에 따라 반환
- **remove(key)**: 해당 버킷에서 key를 찾아 제거

#### 🔹 해시 함수
- `hash(key) = key % SIZE`
- SIZE는 적절한 소수(예: 1000, 769 등)를 사용하는 것이 일반적

---

### 💻 풀이 코드 (Python)

```python
class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = key % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = key % self.size
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
```

---

### ✏️ 마무리 정리

이 문제는 해시 구조의 동작 원리를 잘 이해하고 있어야 풀 수 있다. 
해시 함수, 해시 충돌 처리 방식, 체이닝 등의 개념을 실전에서 구현하며 익힐 수 있다.

기본적인 아이디어는 다음과 같다:
- 버킷 배열을 해시 함수로 접근하고,
- 체이닝(리스트)에 key-value 쌍을 저장하며,
- 삽입, 조회, 삭제 연산 시 해당 체인 리스트에서 순회하며 처리한다.

Python에서는 기본적으로 dict가 모든 기능을 제공하지만, 내부 동작을 직접 구현해보는 연습으로 매우 유익한 문제다.

---

### ✅ 기억해둘 포인트
- 해시 함수는 단순히 `key % N`으로 구성하되, N은 소수나 충분히 큰 값으로 설정
- 해시 충돌 해결은 체이닝 방식 (리스트 활용)
- 시간복잡도는 평균 O(1), 최악 O(n) (동일 버킷에 너무 많은 충돌 시)

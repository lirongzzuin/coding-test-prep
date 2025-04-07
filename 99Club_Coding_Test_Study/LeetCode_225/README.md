## 📦 225. Implement Stack using Queues (LeetCode)

### 📌 문제 설명

Queue(큐) 두 개를 이용해 Stack(스택)을 구현하는 문제입니다. 스택은 LIFO(Last-In-First-Out, 후입선출) 구조이며, 다음 기능을 구현해야 합니다:

- `push(x)`: 원소 `x`를 스택의 맨 위에 추가
- `pop()`: 스택의 맨 위에 있는 원소를 제거하고 반환
- `top()`: 스택의 맨 위에 있는 원소를 조회
- `empty()`: 스택이 비어 있으면 `True`, 아니면 `False` 반환

> 오직 큐의 표준 연산만 사용할 수 있다: `push to back`, `pop from front`, `peek from front`, `size`, `isEmpty`

---

### 🧠 풀이 아이디어

스택과 큐는 기본 동작 방식이 다릅니다. 이를 큐 두 개를 조합하여 **스택의 LIFO 동작을 흉내** 내는 것이 이 문제의 핵심이다.

#### 🔸 스택 vs 큐 구조 차이

| 자료구조 | 동작 방식     | 설명                  |
|----------|--------------|-----------------------|
| 스택     | LIFO         | 마지막에 넣은 값이 먼저 나감 |
| 큐       | FIFO         | 먼저 넣은 값이 먼저 나감   |

---

### 🔧 구현 전략: `push` 시 큐 재배열

- 큐 2개 사용: `q1`(메인 큐), `q2`(임시 큐)
- `push(x)`:
  1. `q2`에 `x` 삽입
  2. `q1`의 모든 요소를 `q2` 뒤에 삽입
  3. `q1`, `q2`를 스왑 → `q1`에 가장 최근 값이 항상 맨 앞에 오도록 유지

- 이후 `pop()`과 `top()` 연산은 `q1`의 front만 확인하면 됨

---

### 💻 코드 구현 (Python)

```python
from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)  # 새 원소는 q2에 먼저 삽입
        while self.q1:
            self.q2.append(self.q1.popleft())  # 기존 원소들을 q2 뒤에 붙임
        self.q1, self.q2 = self.q2, self.q1  # q1이 항상 메인 큐 역할

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1
```

---

### 📊 시간 복잡도

| 연산     | 시간 복잡도 |
|----------|-------------|
| `push`   | O(n)        |
| `pop`    | O(1)        |
| `top`    | O(1)        |
| `empty`  | O(1)        |

---

### ✏️ 요약 정리

- `push` 시 큐 내부 순서를 정렬하여 마지막 삽입 원소가 항상 front에 오도록 유지
- `pop`, `top` 연산은 `main_q`의 front에서 바로 처리 가능
- 두 큐를 활용한 구조는 직관적이며 인터뷰에 자주 등장하는 패턴

---

### ✅ 기억해둘 포인트

- 큐 2개를 사용해 스택의 LIFO 구조를 구현할 수 있다
- `push` 연산에서 큐를 재배열해 스택의 특징을 흉내 낸다
- 한 개의 큐로도 구현 가능하지만, 두 개 사용하는 방식이 더 직관적이다

> 인터뷰에서 자주 등장하는 전형적인 문제, 구조를 이해하고 코드로 구현하는 연습 필요.
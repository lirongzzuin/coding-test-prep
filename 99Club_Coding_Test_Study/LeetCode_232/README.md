# 232. Implement Queue using Stacks (LeetCode) - Day 4

## 📌 문제 설명

스택(Stack) 두 개를 사용하여 큐(Queue)를 구현하는 문제입니다. 큐는 선입선출(FIFO) 구조이며, 다음 네 가지 기능을 구현해야 합니다:

- `push(x)`: 원소 `x`를 큐의 뒤에 삽입
- `pop()`: 큐의 앞에 있는 원소를 제거하고 반환
- `peek()`: 큐의 앞에 있는 원소를 조회
- `empty()`: 큐가 비어 있으면 `True`, 아니면 `False`

> 오직 스택의 기본 연산만 사용할 수 있습니다: `push`, `pop`, `peek`, `isEmpty`, `size`

---

## 🧠 풀이 아이디어

이 문제는 스택 두 개를 이용하여 큐의 선입선출(FIFO) 동작을 흉내 내는 구조를 구현하는 것이 핵심입니다.

### 🔸 사용되는 두 개의 스택

- `in_stack`: 새로 들어오는 원소를 저장 (입력 전용)
- `out_stack`: 원소를 꺼낼 때 사용 (출력 전용)

### 🔸 연산별 동작 방식

| 연산     | 동작 설명 |
|----------|-----------|
| `push(x)` | `in_stack`에 원소를 넣습니다 |
| `pop()`   | `out_stack`이 비어 있으면 `in_stack`의 모든 원소를 꺼내서 뒤집어 저장하고, `out_stack.pop()`을 실행합니다 |
| `peek()`  | `out_stack`이 비어 있으면 `in_stack`에서 옮긴 뒤, `out_stack[-1]`을 반환합니다 |
| `empty()` | 두 스택이 모두 비어 있으면 `True`를 반환합니다 |

---

## 📊 시간 복잡도

- `push`: O(1)
- `pop`, `peek`: **O(1) (평균적으로, amortized)**  
  → `out_stack`이 비어 있을 때만 `in_stack`의 모든 원소를 옮김  
- `empty`: O(1)

---

## 💻 코드 구현 (Python)

```python
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()  # 필요한 경우 in_stack → out_stack 이동
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack
```

---

## 🧾 요약 및 포인트 정리

- 두 개의 스택을 사용하면 큐의 FIFO 구조를 흉내 낼 수 있다.
- 입력은 `in_stack`에, 출력은 `out_stack`에서 처리
- `out_stack`이 비었을 경우에만 `in_stack`의 데이터를 옮긴다.
- 이 구조는 인터뷰에서도 자주 등장하는 문제이므로 반드시 익혀둘 것

> 스택을 사용해 큐를 구현하는 대표적인 문제로, 실전 코딩 테스트와 인터뷰에서 자주 등장합니다. 구조를 이해하고 손으로 구현해보는 연습이 중요합니다.
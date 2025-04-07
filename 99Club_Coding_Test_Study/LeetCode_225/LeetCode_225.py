from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)  # 새 원소는 q2에 먼저 삽입
        while self.q1:
            self.q2.append(self.q1.popleft())  # 기존 원소를 모두 q2 뒤에 붙임
        self.q1, self.q2 = self.q2, self.q1  # q1이 항상 메인 큐 역할

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return not self.q1
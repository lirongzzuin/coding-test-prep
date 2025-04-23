import sys

n, k = sys.stdin.readline().split()
people = set()  # 신청자 중복 제거

for _ in range(int(n)):
    people.add(sys.stdin.readline().rstrip())

p = len(people)  # 유일한 신청자 수

if k == 'Y':
    print(p)
elif k == 'F':
    print(p // 2)
else:  # 'O'
    print(p // 3)
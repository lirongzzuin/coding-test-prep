def is_good_word(word):
    stack = []
    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return not stack

# 입력 처리
n = int(input())
count = 0
for _ in range(n):
    word = input().strip()
    if is_good_word(word):
        count += 1

print(count)
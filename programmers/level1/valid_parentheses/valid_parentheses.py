def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False

    return not stack

if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("([)]"))
    print(is_valid("{[]}"))
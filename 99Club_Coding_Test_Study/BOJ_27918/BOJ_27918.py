def evaluate_expression(expr):
    prefix = 0
    while expr[prefix] == '!':
        prefix += 1

    n = int(expr[prefix])

    suffix = len(expr) - (prefix + 1)

    for _ in range(suffix):
        n = 1 

    for _ in range(prefix):
        n = 0 if n == 1 else 1

    return n

# 입력 처리
T = int(input())
for _ in range(T):
    expr = input().strip()
    print(evaluate_expression(expr))
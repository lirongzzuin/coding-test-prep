def find_pattern(filenames):
    pattern = list(filenames[0])

    for filename in filenames[1:]:
        for i in range(len(pattern)):
            if pattern[i] != filename[i]:
                pattern[i] = '?'

    return ''.join(pattern)

n = int(input())
filenames = [input().strip() for _ in range(n)]

print(find_pattern(filenames))

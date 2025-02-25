def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))
    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))

def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1

    compressed.append(f"{s[-1]}{count}") 
    return "".join(compressed)

if __name__ == "__main__":
    print(compress_string("aaabbcddd"))  
    print(compress_string("abcd")) 
    print(compress_string("aaabbaa"))  

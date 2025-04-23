class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seen = set()
        output = set()

        for i in range(len(s) - 9):  # 길이 10짜리 윈도우
            sub = s[i:i+10]
            if sub in seen:
                output.add(sub)
            else:
                seen.add(sub)

        return list(output)
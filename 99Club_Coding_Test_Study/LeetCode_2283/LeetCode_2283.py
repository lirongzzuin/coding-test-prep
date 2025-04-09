class Solution(object):
    def digitCount(self, num):
        count = [0] * 10  # 0부터 9까지 숫자 카운트용

        for ch in num:
            count[int(ch)] += 1

        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False

        return True
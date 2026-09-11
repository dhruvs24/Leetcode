class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0
        seen = [False] * 1000
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if j == i:
                    continue
                for k in range(len(digits)):
                    if k == i or k == j or digits[k] % 2 != 0:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not seen[num]:
                        seen[num] = True
                        count += 1
        return count  
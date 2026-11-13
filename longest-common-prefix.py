class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        min_string = min(strs)
        max_string = max(strs)

        for i in range(len(min_string)):
            if min_string[i] == max_string[i]:
                res += min_string[i]
            else:
                return res
        return res
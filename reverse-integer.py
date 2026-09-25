class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        sign = -1 if x < 0 else 1

        x_rev_str = str(abs(x))[::-1]
        x_rev = int(x_rev_str)

        if x_rev <= MAX_INT and x_rev >= MIN_INT:
            return sign * x_rev
        return 0
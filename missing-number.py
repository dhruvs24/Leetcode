class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = n * (n + 1) / 2 # Gaussian Sum
        actual = 0
        for num in nums:
            actual += num
        return expected - actual
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left + 1, right + 1]
            if two_sum < target:
                left += 1
            if two_sum > target:
                right -= 1
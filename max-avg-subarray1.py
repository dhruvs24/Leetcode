class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = k - 1
        curr_sum = 0
        for i in range(right + 1):
            curr_sum += nums[i]   
        greatest = curr_sum

        while right < len(nums) - 1:
            curr_sum -= nums[left]
            curr_sum += nums[right + 1]
            greatest = max(greatest, curr_sum)
            left += 1
            right +=1

        return greatest / k
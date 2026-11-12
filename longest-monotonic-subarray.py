class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        max_length = 1
        incr_length = 1
        decr_length = 1
        for right in range(1, len(nums)):
            if nums[right] > nums[left]:
                incr_length += 1
                decr_length = 1
                
            elif nums[right] < nums[left]:
                decr_length += 1
                incr_length = 1
                
            elif nums[right] == nums[left]:
                
                incr_length = 1
                decr_length = 1
               
            max_length = max(max_length, incr_length, decr_length)
            left += 1
            
        return max_length
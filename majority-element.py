class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0 # Boyer-Moore Voting Algorithm
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

# if majority element not guarenteed:
if nums.count(candidate) > len(nums) // 2:
    return candidate
return None
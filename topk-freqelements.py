# Suboptimal solution O(nlogn) time
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for i in range(len(nums)):
            if nums[i] in num_to_freq:
                num_to_freq[nums[i]] += 1
            else:
                num_to_freq[nums[i]] = 1
        
        array = []
        for key, value in num_to_freq.items():
            array.append((key, value))
        sorted_array = sorted(array, key=lambda x: x[1], reverse=True)
        
        result_array = []
        for i in range(0, k):
            result_array.append(sorted_array[i][0])
        
        return result_array
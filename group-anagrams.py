class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for c in string:
                freq[ord(c) - ord('a')] += 1
            result[tuple(freq)].append(string)
        return list(result.values())
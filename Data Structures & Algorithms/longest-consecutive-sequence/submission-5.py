class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sequence = set(nums)
        for  n in sequence:
            length = 0
            if n-1 in sequence:
                continue
            while n + length in sequence:
                length+=1
                longest = max(length, longest)
        return longest
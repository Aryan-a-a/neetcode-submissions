class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        longest = 0
        for n in nums:
            length = 0
            if (n-1) in count:
                continue
            while(n + length) in count:
                length +=1
            longest = max(longest,length)
        return longest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        mostFreq = []
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        sortedKeys = sorted(count, key=count.get, reverse=True)
        return sortedKeys[:k]

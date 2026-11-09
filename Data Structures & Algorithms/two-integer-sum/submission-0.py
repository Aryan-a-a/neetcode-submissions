class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in sum:
                return [sum[result], i]
            sum[nums[i]] = i
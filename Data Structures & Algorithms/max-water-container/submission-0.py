class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaMax = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = (r-l) * min(heights[r],heights[l])
            if heights[l] > heights[r]:
                r-=1
            else: 
                heights[l] < heights[r]
                l+=1
            areaMax = max(areaMax, area)
        return areaMax                
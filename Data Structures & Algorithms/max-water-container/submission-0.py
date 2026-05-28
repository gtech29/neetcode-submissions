# Find the max amount of water any two bars can hold
# 
# input
# heights = [1,7,2,5,4,7,3,6]
# V = (j - i) * min(heights[i], heights[j])
# 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        max_area = 0

        while i < j:
            V = (j - i) * min(heights[i], heights[j])
            if V > max_area:
                max_area = V

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
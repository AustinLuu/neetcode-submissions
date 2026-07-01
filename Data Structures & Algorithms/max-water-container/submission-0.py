class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, (len(heights) - 1)
        max_area = 0 
        while l < r:
            l_height = heights[l]
            r_height = heights[r]
            area = min(l_height, r_height) * (r-l)
            if area > max_area:
                max_area = area
            if l_height > r_height:
                r-=1
            else:
                l+=1
        return max_area
            
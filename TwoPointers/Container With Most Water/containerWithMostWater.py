def maxArea(self, height: List[int]) -> int:
    maxArea = -99999
    l, r = 0, len(height) - 1
    while (l < r):
        area = min(height[l], height[r]) * abs(l - r)
        maxArea = max(area, maxArea)
        if height[l] < height[r]:
            l += 1
        else:
             r -= 1
    return maxArea 

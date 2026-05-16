class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            width = right - left
            adj_height = min(heights[left],heights[right])
            area = width * adj_height
            max_area = max(max_area,area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
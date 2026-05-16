class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    break
                right = i
                width = right - left - 1
                adj_height = min(height[left],height[right]) - height[mid]
                max_area += (width * adj_height)
            stack.append(i)
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        answer = 0
        heights.append(float('-inf'))

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                mid = stack.pop()
                left = stack[-1] if stack else -1
                width = i - left - 1
                area = width * heights[mid]
                answer = max(answer,area)
            stack.append(i)
        return answer
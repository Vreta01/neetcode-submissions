class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[mid][-1]:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                left2 = 0
                right2 = n - 1
                while(left2 <= right2):
                    mid2 = left2 + (right2 - left2) // 2
                    if target == matrix[mid][mid2]:
                        return True
                    elif target < matrix[mid][mid2]:
                        right2 = mid2 - 1
                    else:
                        left2 = mid2 + 1
                return False
        return False
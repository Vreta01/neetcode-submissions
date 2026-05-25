class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = 0
        def can_finish(speed):
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed
                if h < time:
                    return False
            return True
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

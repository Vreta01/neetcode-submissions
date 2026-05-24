class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.answer = []
        left = 0
        n = len(nums)
        self.heap = []
        def find_max():
            heapq.heapify(self.heap)
            self.answer.append(-self.heap[0])
        for i in range(k):
            self.heap.append(-nums[i])
        find_max()
        for i in range(k,n):
            self.heap.remove(-nums[left])
            left += 1
            self.heap.append(-nums[i])
            find_max()
        return self.answer


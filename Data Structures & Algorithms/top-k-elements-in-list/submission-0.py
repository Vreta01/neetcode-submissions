class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        for num, count in counts.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count,num in heap]
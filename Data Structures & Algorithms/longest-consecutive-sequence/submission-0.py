class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        longest = 0

        for num in vals:
            if num - 1 not in vals:
                length = 1

                while num + length in vals:
                    length += 1
                longest = max(longest,length)
        return longest
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left = 1
        for i in range(len(nums)):
            output[i] = left
            left = output[i] * nums[i]

        right = 1
        for i in range(len(nums) -1,-1,-1):
            output[i] = right * output[i]
            right *= nums[i]
        return output  
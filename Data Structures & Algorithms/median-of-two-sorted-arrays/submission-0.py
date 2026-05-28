class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = 0,len(nums1)

        while True:
            i = (left + right) // 2
            j = half - i
            aleft = nums1[i-1] if i > 0 else float('-inf')
            aright = nums1[i] if i < len(nums1) else float('inf')
            bleft = nums2[j-1] if j > 0 else float('-inf')
            bright = nums2[j] if j < len(nums2) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright,bright)
                else:
                    return ( max(aleft,bleft) + min(aright,bright) )/ 2
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1
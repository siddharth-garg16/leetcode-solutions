class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        lo = 0
        hi = len(nums1)
        half = (len(nums1) + len(nums2) + 1) // 2
        midA = (hi + lo) // 2

        while hi >= lo:
            midA = (hi + lo) // 2
            midB = half - midA

            leftA = nums1[midA - 1] if midA > 0 else float('-inf')
            leftB = nums2[midB - 1] if midB > 0 else float('-inf')

            rightA = nums1[midA] if midA < len(nums1) else float('inf')
            rightB = nums2[midB] if midB < len(nums2) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            elif leftA > rightB:
                hi = midA - 1
            else:
                lo = midA + 1

        return -1




    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     num = [*nums1, *nums2]
    #     num.sort()
    #     n = len(num)
    #     if n % 2 != 0:
    #         return num[(int((n + 1) // 2) - 1)]
    #     else:
    #         return (num[int((n // 2) - 1)] + num[int(((n + 1) // 2))]) / 2
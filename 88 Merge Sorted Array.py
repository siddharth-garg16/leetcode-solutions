class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #O(nlogn)
        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()



        # O(m+n) solution using three pointer method
        # p1, p2 = m - 1, n - 1
        # ip = len(nums1) - 1
        #
        # while p2 >= 0:
        #     if nums2[p2] <= nums1[p1] and p1 >= 0:
        #         nums1[ip] = nums1[p1]
        #         nums1[p1] = 0
        #         p1 -= 1
        #         ip -= 1
        #         continue
        #
        #     nums1[ip] = nums2[p2]
        #     p2 -= 1
        #     ip -= 1
        #     continue
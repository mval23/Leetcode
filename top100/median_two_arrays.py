class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total//2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r)//2 # nums1
            j = half - i - 2 # nums2

            n1left = nums1[i] if i >= 0 else float("-infinity")
            n1right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            n2left = nums2[j] if j >= 0 else float("-infinity")
            n2right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            # partition :)
            if n1left <= n2right and n2left <= n1right:
                # odd
                if total % 2:
                    return min(n1right, n2right)
                # even
                return max(n1left, n2left) + min(n1right, n2right)/2
            elif n1left > n2right:
                r = i - 1
            else:
                l = i + 1






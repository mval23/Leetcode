class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([3,3], 6))
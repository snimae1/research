class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalProduct = 1
        for x in nums:
            totalProduct *= x

        leftSum = 0
        rightProduct = totalProduct

        for i in range(len(nums)):
            rightProduct //= nums[i]

            if leftSum == rightProduct:
                return i

            leftSum += nums[i]

        return -1

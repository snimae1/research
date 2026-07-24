class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        # The rightmost element (index n-1) has no elements to its right, so skip it.
        for i in range(n - 1):
            right_sum = sum(nums[i+1:])
            right_count = n - i - 1
            # Avoid floating-point comparison: nums[i] > right_sum / right_count
            # is equivalent to nums[i] * right_count > right_sum
            if nums[i] * right_count > right_sum:
                count += 1
        return count

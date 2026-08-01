class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        asc_sum = 0

        # Strictly increasing part: sum all elements before the peak
        while i + 1 < n and nums[i] < nums[i + 1]:
            asc_sum += nums[i]
            i += 1

        # i is now the index of the peak element
        peak = nums[i]
        asc_sum += peak          # include peak in ascending sum

        # Descending part: start with peak, then add the rest
        desc_sum = peak
        for j in range(i + 1, n):
            desc_sum += nums[j]

        # Compare the two sums
        if asc_sum > desc_sum:
            return 0
        elif desc_sum > asc_sum:
            return 1
        else:
            return -1

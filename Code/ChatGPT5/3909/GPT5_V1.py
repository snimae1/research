class Solution(object):
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the peak index
        peak = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[peak]:
                peak = i
            else:
                break

        # Sum of ascending part (including peak)
        ascending_sum = sum(nums[:peak + 1])

        # Sum of descending part (including peak)
        descending_sum = sum(nums[peak:])

        # Compare the sums
        if ascending_sum > descending_sum:
            return 0
        elif descending_sum > ascending_sum:
            return 1
        else:
            return -1

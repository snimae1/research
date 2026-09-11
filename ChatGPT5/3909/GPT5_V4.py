"""Solution for comparing the sums of the two parts of a bitonic array."""

# pylint: disable=too-few-public-methods


class Solution:
    """Compare the sums of the ascending and descending parts."""

    # The method name is fixed by the programming task.
    # pylint: disable=invalid-name
    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak = 0

        # Find the peak element.
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                peak = index
            else:
                break

        # Calculate both sums. The peak belongs to both parts.
        ascending_sum = sum(nums[:peak + 1])
        descending_sum = sum(nums[peak:])

        # Compare the two sums.
        if ascending_sum > descending_sum:
            return 0

        if descending_sum > ascending_sum:
            return 1

        return -1

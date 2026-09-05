"""
Module for solving the sortable integers problem.
"""

class Solution:
    """Solution class containing the sortableIntegers method."""

    # pylint: disable=invalid-name
    def sortableIntegers(self, nums):
        """
        Return the sum of all sortable k values for the given array.

        A k is sortable if we can partition the array into blocks of size k,
        cyclically rotate each block independently to make it sorted,
        and the concatenated blocks result in a sorted array.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0

        # Check every divisor of n
        for k in range(1, n + 1):
            if n % k == 0 and self._is_sortable_k(nums, k):
                total += k

        return total

    def _is_sortable_k(self, nums, k):
        """
        Check if a specific k is sortable.

        :param nums: input array
        :param k: block size
        :return: True if k is sortable, False otherwise
        """
        n = len(nums)
        m = n // k
        block_mins = []
        block_maxs = []

        # Verify each block can be cyclically rotated to sorted order
        for i in range(m):
            start = i * k
            end = start + k
            if not self._is_block_rotatable(nums, start, end):
                return False
            block_mins.append(min(nums[start:end]))
            block_maxs.append(max(nums[start:end]))

        # Check that blocks are correctly ordered (max of previous <= min of next)
        for i in range(m - 1):
            if block_maxs[i] > block_mins[i + 1]:
                return False

        return True

    def _is_block_rotatable(self, nums, start, end):
        """
        Check if the subarray nums[start:end] can be cyclically rotated to be sorted.

        A subarray can be sorted by cyclic rotation iff it has at most one "drop"
        when traversed linearly (including the wrap-around from last to first).

        :param nums: input array
        :param start: start index (inclusive)
        :param end: end index (exclusive)
        :return: True if the block is rotatable to sorted order, False otherwise
        """
        drops = 0

        # Check drops between consecutive elements inside the block
        for j in range(start, end - 1):
            if nums[j] > nums[j + 1]:
                drops += 1
                if drops > 1:
                    return False

        # Check wrap-around drop (last element to first element)
        if nums[end - 1] > nums[start]:
            drops += 1

        return drops <= 1

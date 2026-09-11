"""Solution for finding the minimum cost to make two arrays identical."""

from collections import Counter


class Solution(object):  # pylint: disable=useless-object-inheritance,too-few-public-methods
    """Provide a solution for the minimum-cost array transformation problem."""

    def minCost(self, nums1, nums2):  # pylint: disable=invalid-name
        """
        Return the minimum cost required to make nums1 and nums2 identical.

        Free swaps are allowed within each array. A swap between nums1[i]
        and nums2[i] costs one unit.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        total_count = Counter(nums1)
        total_count.update(nums2)

        # Every value must occur an even number of times overall.
        if any(count % 2 != 0 for count in total_count.values()):
            return -1

        difference = Counter(nums1)
        difference.subtract(nums2)

        # Count how many elements must move from nums1 to nums2.
        required_swaps = sum(
            count // 2
            for count in difference.values()
            if count > 0
        )

        # A paid swap can only help at a mismatched position.
        mismatched_positions = sum(
            value1 != value2
            for value1, value2 in zip(nums1, nums2)
        )

        if required_swaps > mismatched_positions:
            return -1

        return required_swaps

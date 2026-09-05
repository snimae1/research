# pylint: disable=invalid-name, too-few-public-methods
"""
Module for solving the minimum capacity box problem.
"""

class Solution:
    """
    Solution class for the minimum capacity box problem.
    """

    def minimumIndex(self, capacity, itemSize):
        """
        Find the index of the box with the minimum capacity that can store the item.

        Args:
            capacity (List[int]): List of box capacities.
            itemSize (int): Size of the item to store.

        Returns:
            int: Index of the box with minimum sufficient capacity, or -1 if none.
        """
        min_capacity = float('inf')
        min_index = -1

        for i, cap in enumerate(capacity):
            if itemSize <= cap < min_capacity:
                min_capacity = cap
                min_index = i

        return min_index

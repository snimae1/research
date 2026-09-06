"""Solution for finding valid elements in an integer array."""
# pylint: disable=invalid-name, too-few-public-methods


class Solution:
    """Provides method to find valid elements according to the problem statement."""

    def findValidElements(self, nums):
        """
        Return all elements that are strictly greater than all elements to their left
        or to their right, or that are the first or last element.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        # left_max[i] enthält das Maximum aller Elemente links von i
        left_max = [0] * n
        current_max = float('-inf')
        for i in range(n):
            left_max[i] = current_max
            if nums[i] > current_max:
                current_max = nums[i]

        # right_max[i] enthält das Maximum aller Elemente rechts von i
        right_max = [0] * n
        current_max = float('-inf')
        for i in range(n - 1, -1, -1):
            right_max[i] = current_max
            if nums[i] > current_max:
                current_max = nums[i]

        result = []
        for i in range(n):
            # Erstes und letztes Element sind immer gültig
            if i in (0, n - 1):
                result.append(nums[i])
            # Ansonsten prüfen, ob eine der beiden Bedingungen erfüllt ist
            elif nums[i] > left_max[i] or nums[i] > right_max[i]:
                result.append(nums[i])

        return result

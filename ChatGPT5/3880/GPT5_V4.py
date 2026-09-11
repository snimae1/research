"""Find the minimum index difference between a 1 and a 2."""


class Solution:
    """Solve the minimum absolute difference problem."""

    # pylint: disable=invalid-name
    def minAbsoluteDifference(self, nums):
        """
        Find the minimum absolute difference between indices of 1 and 2.

        :param nums: List containing only the values 0, 1, and 2.
        :return: Minimum absolute difference, or -1 if no valid pair exists.
        """
        last_one = -1
        last_two = -1
        minimum_difference = float("inf")

        for index, value in enumerate(nums):
            if value == 1:
                last_one = index

                if last_two != -1:
                    difference = index - last_two
                    minimum_difference = min(
                        minimum_difference, difference
                    )

            elif value == 2:
                last_two = index

                if last_one != -1:
                    difference = index - last_one
                    minimum_difference = min(
                        minimum_difference, difference
                    )

        if minimum_difference == float("inf"):
            return -1

        return minimum_difference

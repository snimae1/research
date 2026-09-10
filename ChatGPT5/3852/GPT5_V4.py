"""Find the smallest pair of values with different frequencies."""


class Solution:
    """Solve the minimum distinct frequency pair problem."""

    def minDistinctFreqPair(self, nums):
        """
        Find the smallest pair of distinct values with different frequencies.

        :param nums: List of integers.
        :return: List containing the two selected values, or [-1, -1].
        """
        frequencies = {}

        # Count how often each value occurs.
        for number in nums:
            frequencies[number] = frequencies.get(number, 0) + 1

        # Sort the values to find the smallest valid pair.
        values = sorted(frequencies)

        for index, first_value in enumerate(values):
            for second_value in values[index + 1:]:
                if frequencies[first_value] != frequencies[second_value]:
                    return [first_value, second_value]

        return [-1, -1]

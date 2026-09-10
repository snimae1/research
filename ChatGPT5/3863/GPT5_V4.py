"""Solution for the minimum operations required to sort a string."""


# pylint: disable=too-few-public-methods
class Solution:
    """Provide the solution required by the online judge."""

    # pylint: disable=invalid-name
    def minOperations(self, s):
        """
        Return the minimum number of substring-sorting operations.

        :type s: str
        :rtype: int
        """
        # Check whether the string is already sorted.
        is_sorted = all(
            s[index] <= s[index + 1]
            for index in range(len(s) - 1)
        )

        if is_sorted:
            return 0

        # For two characters, sorting the complete string is not allowed.
        if len(s) == 2:
            return -1

        minimum_char = min(s)
        maximum_char = max(s)

        # One operation is enough if the minimum is at the beginning
        # or the maximum is already at the end.
        if s[0] == minimum_char or s[-1] == maximum_char:
            return 1

        # If the minimum or maximum is somewhere in the middle,
        # two operations are sufficient.
        for char in s[1:-1]:
            if char == minimum_char or char == maximum_char:
                return 2

        # In all other cases, three operations are necessary.
        return 3

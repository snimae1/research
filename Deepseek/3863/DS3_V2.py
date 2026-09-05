"""Solution for LeetCode problem: Minimum Operations to Sort String."""

# pylint: disable=too-few-public-methods, useless-object-inheritance
class Solution(object):
    """Provides method to compute minimum operations to sort string."""

    # pylint: disable=invalid-name
    def minOperations(self, s):
        """
        Return the minimum number of operations to make s sorted,
        or -1 if impossible.

        :type s: str
        :rtype: int
        """
        n = len(s)

        # A single character is already sorted.
        if n == 1:
            return 0

        # With two characters, the only possible substring is the whole string,
        # which is not allowed. Thus impossible if not already sorted.
        if n == 2:
            return 0 if s[0] <= s[1] else -1

        # Determine global minimum and maximum characters.
        min_char = min(s)
        max_char = max(s)

        # Early exit if the string is already sorted.
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # If the first character is already the smallest, sorting the rest suffices.
        if s[0] == min_char:
            return 1

        # If the last character is already the largest, sorting the prefix suffices.
        if s[-1] == max_char:
            return 1

        # Check whether an extreme character appears elsewhere,
        # which would allow us to fix one endpoint in the first operation.
        min_not_only_last = any(ch == min_char for ch in s[:-1])
        max_not_only_first = any(ch == max_char for ch in s[1:])

        # If we can fix one endpoint, two operations are enough.
        if min_not_only_last or max_not_only_first:
            return 2

        # Otherwise the only occurrence of the minimum is at the end and the only
        # occurrence of the maximum is at the beginning; three operations are needed.
        return 3

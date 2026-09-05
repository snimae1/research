"""Module providing a solution to the first matching index problem."""

class Solution:
    """Solution class for LeetCode problem."""

    # pylint: disable=too-few-public-methods
    # pylint: disable=invalid-name
    def firstMatchingIndex(self, s):
        """
        Find the smallest index i such that s[i] == s[n - i - 1].

        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i
        return -1

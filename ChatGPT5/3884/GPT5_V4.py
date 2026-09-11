"""Find the first index whose character matches its mirrored character."""


class Solution:
    """Provide a solution for finding the first matching index."""

    def firstMatchingIndex(self, s):
        """
        Find the smallest index i where s[i] equals s[n - i - 1].

        :param s: String consisting of lowercase English letters.
        :return: The smallest matching index, or -1 if none exists.
        """
        n = len(s)

        for i in range(n):
            if s[i] == s[n - i - 1]:
                return i

        return -1

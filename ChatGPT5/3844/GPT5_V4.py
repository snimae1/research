"""Find the longest substring that becomes a palindrome after one deletion."""


class Solution:
    """Solution for finding the longest almost-palindromic substring."""

    def almostPalindromic(self, s):
        """
        Return the length of the longest almost-palindromic substring.

        :param s: String containing lowercase English letters.
        :return: Length of the longest almost-palindromic substring.
        """
        n = len(s)

        # palindrome[i][j] is True if s[i:j + 1] is a palindrome.
        palindrome = [[False] * n for _ in range(n)]

        # Every single character is a palindrome.
        for i in range(n):
            palindrome[i][i] = True

        # Build the palindrome table from short substrings to long ones.
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    palindrome[left][right] = (
                        length == 2 or palindrome[left + 1][right - 1]
                    )

        longest = 1

        # Check every possible substring.
        for left in range(n):
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    # The substring is already a palindrome.
                    if palindrome[left][right]:
                        longest = max(longest, right - left + 1)

                elif (
                    palindrome[left + 1][right]
                    or palindrome[left][right - 1]
                ):
                    # Remove either the left or the right character.
                    longest = max(longest, right - left + 1)

        return longest

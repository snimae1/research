"""
Module for finding the longest almost-palindromic substring.

An almost-palindromic substring becomes a palindrome after removing exactly
one character.
"""

class Solution:
    """
    Provides a method to compute the length of the longest almost-palindromic
    substring in a given string.
    """

    def almostPalindromic(self, s: str) -> int:
        """
        Returns the length of the longest substring that can become a palindrome
        by deleting exactly one character.

        Args:
            s (str): Input string of lowercase English letters.

        Returns:
            int: Maximum length of an almost-palindromic substring.
        """
        n = len(s)
        if n < 2:
            return n

        # is_pal[i][j] == 1  ->  substring s[i:j+1] is a palindrome
        # is_almost[i][j] == 1 -> substring s[i:j+1] is almost-palindromic
        is_pal = [bytearray(n) for _ in range(n)]
        is_almost = [bytearray(n) for _ in range(n)]

        max_len = 1

        # Base case: length 1
        for i in range(n):
            is_pal[i][i] = 1
            is_almost[i][i] = 1

        # DP over increasing substring lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check if s[i:j+1] is a palindrome
                if s[i] == s[j]:
                    if length == 2:
                        is_pal[i][j] = 1
                    else:
                        is_pal[i][j] = is_pal[i + 1][j - 1]

                # Determine if s[i:j+1] is almost-palindromic
                if is_pal[i][j]:
                    # Already a palindrome, so it's also almost-palindromic
                    is_almost[i][j] = 1
                else:
                    if s[i] == s[j]:
                        # Equal ends: we can remove one character inside
                        if length > 2 and is_almost[i + 1][j - 1]:
                            is_almost[i][j] = 1
                    else:
                        # Different ends: we must remove either left or right end
                        if is_pal[i + 1][j] or is_pal[i][j - 1]:
                            is_almost[i][j] = 1

                if is_almost[i][j]:
                    max_len = max(max_len, length)

        return max_len

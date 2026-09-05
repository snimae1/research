"""
This module provides a solution to find the longest almost-palindromic substring.
A substring is almost-palindromic if it becomes a palindrome after removing
exactly one character.
"""

class Solution:
    """
    Class containing the logic to solve the almost-palindromic substring problem.
    """

    def almostPalindromic(self, s): # pylint: disable=invalid-name
        """
        Finds the length of the longest substring that becomes a palindrome
        after removing exactly one character.

        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0

        # is_palindrome[i][j] is True if s[i...j] is a perfect palindrome.
        # We use a 2D array to store results of sub-problems (Dynamic Programming).
        is_palindrome = [[False] * n for _ in range(n)]

        # All single characters are palindromes by definition.
        for i in range(n):
            is_palindrome[i][i] = True

        # Check all substrings of length 2.
        for i in range(n - 1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1] = True

        # Fill the DP table for strings of length 3 up to n.
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i+1][j-1]:
                    is_palindrome[i][j] = True

        max_len = 0

        # We iterate through every possible center of a palindrome (2n-1 centers).
        for center in range(2 * n - 1):
            # left and right are the boundaries of the expansion.
            left = center // 2
            right = left + (center % 2)

            # Expand outwards as long as the characters match (perfect palindrome).
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                # Any palindrome of length >= 2 is 'almost-palindromic' because
                # removing the middle character leaves a palindrome.
                if current_len >= 2:
                    max_len = max(max_len, current_len)
                left -= 1
                right += 1

            # After the while-loop, s[left] != s[right].
            # We check if this substring is 'almost-palindromic' by removing
            # either the leftmost or the rightmost character.
            if left >= 0 and right < n:
                # If removing one character results in a palindrome, it's valid.
                if is_palindrome[left + 1][right] or is_palindrome[left][right - 1]:
                    max_len = max(max_len, right - left + 1)

        # If no larger substring is found, the minimum possible almost-palindromic
        # length for n >= 2 is 2 (any two chars, remove one -> length 1 palindrome).
        return max(max_len, 2 if n >= 2 else 0)

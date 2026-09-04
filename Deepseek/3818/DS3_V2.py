"""
Module for solving the reverse by type problem.
"""

# pylint: disable=too-few-public-methods, useless-object-inheritance
class Solution(object):
    """
    Provides a method to reverse lowercase letters and special characters separately.
    """

    # pylint: disable=invalid-name
    def reverseByType(self, s):
        """
        Reverse lowercase letters and special characters separately.

        :type s: str
        :rtype: str
        """
        letters = [c for c in s if c.isalpha()]
        specials = [c for c in s if not c.isalpha()]

        letters.reverse()
        specials.reverse()

        result = []
        letter_idx = 0
        special_idx = 0

        for char in s:
            if char.isalpha():
                result.append(letters[letter_idx])
                letter_idx += 1
            else:
                result.append(specials[special_idx])
                special_idx += 1

        return ''.join(result)

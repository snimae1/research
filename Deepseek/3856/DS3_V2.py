"""
Module for trimming trailing vowels from a string.
"""

class Solution(object):
    """
    Provides a method to remove trailing vowels from a string.
    """
    def trimTrailingVowels(self, s):
        """
        Removes all trailing vowels from the input string.

        :param s: Input string consisting of lowercase English letters.
        :type s: str
        :return: String with trailing vowels removed.
        :rtype: str
        """
        return s.rstrip('aeiou')

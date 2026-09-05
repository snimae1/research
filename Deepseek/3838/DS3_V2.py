"""
Module for mapping word weights to characters.
"""

class Solution:  # pylint: disable=too-few-public-methods
    """
    Solution class for the word weight mapping problem.
    """

    def mapWordWeights(self, words, weights):  # pylint: disable=invalid-name
        """
        Map each word's weight to a character based on modulo 26.

        :param words: List of strings
        :param weights: List of 26 integers representing letter weights
        :return: Concatenated string of mapped characters
        """
        result = []
        for word in words:
            # Sum the weights of the characters in the word
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            # Modulo 26 and map to reverse alphabetical order: 0->z, 1->y, ..., 25->a
            mapped_char = chr(ord('z') - (total % 26))
            result.append(mapped_char)
        return ''.join(result)

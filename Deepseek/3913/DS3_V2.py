"""
Solution for the problem: Rearrange vowels in a string by frequency.
"""


class Solution(object):
    """
    Provides a method to rearrange vowels in a string based on frequency.
    """

    # pylint: disable=too-few-public-methods
    # pylint: disable=useless-object-inheritance
    def sortVowels(self, s):
        # pylint: disable=invalid-name
        """
        Rearranges the vowels in the input string.

        Vowels are sorted in non-increasing order of their frequency in the
        original string. If two vowels have the same frequency, they are
        ordered by their position of first occurrence.

        Args:
            s (str): Input string consisting of lowercase English letters.

        Returns:
            str: Modified string with vowels rearranged.
        """
        vowels = set('aeiou')
        vowel_indices = [i for i, ch in enumerate(s) if ch in vowels]

        if not vowel_indices:
            return s

        vowel_chars = [s[i] for i in vowel_indices]

        # Collect frequency and first occurrence for each distinct vowel
        vowel_info = []
        for v in set(vowel_chars):
            freq = s.count(v)
            first_pos = s.find(v)
            vowel_info.append((v, freq, first_pos))

        # Sort by frequency (descending) and then by first occurrence (ascending)
        vowel_info.sort(key=lambda x: (-x[1], x[2]))

        # Build the sorted list of vowels
        sorted_vowels = []
        for v, freq, _ in vowel_info:
            sorted_vowels.extend([v] * freq)

        # Place sorted vowels back into original vowel positions
        result = list(s)
        for idx, ch in zip(vowel_indices, sorted_vowels):
            result[idx] = ch

        return "".join(result)

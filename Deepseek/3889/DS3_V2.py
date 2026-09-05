"""
Solution for the mirror frequency problem.
"""

from collections import Counter

class Solution(object):
    """
    Provides a method to compute the total absolute difference between
    frequencies of characters and their mirror counterparts.
    """

    def _get_mirror(self, char):
        """
        Return the mirror character of the given character.

        For lowercase letters, the mirror is the letter at the same position
        from the end of the alphabet. For digits, it is the digit at the same
        position from the end of the range '0' to '9'.
        """
        if 'a' <= char <= 'z':
            return chr(ord('z') - (ord(char) - ord('a')))
        # char is a digit
        return chr(ord('9') - (ord(char) - ord('0')))

    def mirrorFrequency(self, s):
        """
        Calculate the sum of |freq(c) - freq(m)| over all distinct mirror pairs.

        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        visited = set()
        total = 0

        for char in freq:
            if char in visited:
                continue

            mirror = self._get_mirror(char)
            total += abs(freq[char] - freq.get(mirror, 0))

            # Mark both characters of the pair as processed to avoid double counting
            visited.add(char)
            visited.add(mirror)

        return total

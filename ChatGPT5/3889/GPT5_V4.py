"""Calculate the total frequency difference of mirror character pairs."""

from collections import Counter


class Solution(object):
    """Provide the solution for the mirror frequency problem."""

    def mirrorFrequency(self, s):
        """
        Calculate the sum of frequency differences for mirror pairs.

        :param s: String containing lowercase letters and digits.
        :return: Sum of absolute frequency differences.
        """
        frequencies = Counter(s)
        total = 0

        # Process each mirror pair only once.
        for character in frequencies:
            if "a" <= character <= "z":
                mirror = chr(ord("z") - (ord(character) - ord("a")))
            else:
                mirror = chr(ord("9") - (ord(character) - ord("0")))

            # Only process one direction of each mirror pair.
            if character <= mirror:
                total += abs(
                    frequencies[character] - frequencies.get(mirror, 0)
                )

        return total

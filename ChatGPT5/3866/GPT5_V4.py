"""Lösung zum Finden der ersten einzigartigen geraden Zahl."""

# Die Namen sind durch die Aufgabenplattform vorgegeben.
# pylint: disable=invalid-name,too-few-public-methods


class Solution:
    """Enthält die Lösung für die gestellte Array-Aufgabe."""

    def firstUniqueEven(self, nums):
        """
        Findet die erste gerade Zahl, die genau einmal vorkommt.

        :type nums: List[int]
        :rtype: int
        """
        frequencies = {}

        # Häufigkeit jeder Zahl zählen.
        for number in nums:
            frequencies[number] = frequencies.get(number, 0) + 1

        # Erste gerade Zahl suchen, die genau einmal vorkommt.
        for number in nums:
            if number % 2 == 0 and frequencies[number] == 1:
                return number

        return -1

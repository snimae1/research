"""
Dieses Modul bietet eine Lösung, um das erste Element in einer Liste
zu finden, dessen Häufigkeit innerhalb der Liste einzigartig ist.
"""
from collections import Counter


class Solution:
    """
    Klasse zur Berechnung der ersten Zahl mit einer eindeutigen Frequenz.
    """

    # pylint: disable=invalid-name
    def firstUniqueFreq(self, nums):
        """
        Findet das erste Element von links nach rechts, dessen
        Vorkommenshäufigkeit im Array einzigartig ist.

        :type nums: List[int]
        :rtype: int
        """
        # Schritt 1: Zähle die Häufigkeit jedes Elements im Array
        # Beispiel [20, 10, 30, 30] -> {20: 1, 10: 1, 30: 2}
        counts = Counter(nums)

        # Schritt 2: Zähle, wie oft jede Häufigkeit vorkommt
        # Beispiel {20: 1, 10: 1, 30: 2} -> Frequenzen sind [1, 1, 2]
        # freq_counts wird dann: {1: 2, 2: 1}
        freq_counts = Counter(counts.values())

        # Schritt 3: Gehe das Array von links nach rechts durch
        for num in nums:
            # Ermittle die Häufigkeit der aktuellen Zahl
            f = counts[num]
            # Wenn diese Häufigkeit nur genau ein einziges Mal vorkommt,
            # ist sie eindeutig (unique).
            if freq_counts[f] == 1:
                return num

        # Falls kein Element mit einer eindeutigen Häufigkeit gefunden wurde
        return -1


# pylint: disable=too-few-public-methods

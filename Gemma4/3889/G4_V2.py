"""
Dieses Modul bietet eine Lösung zur Berechnung der Mirror-Frequenzen
von Zeichen (Buchstaben und Ziffern) in einem gegebenen String.
"""
from collections import Counter

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Lösung des Mirror-Frequency Problems.
    Berechnet die Summe der absoluten Differenzen zwischen
    Zeichen und ihren jeweiligen Spiegelbildern.
    """

    def mirror_frequency(self, s):
        """
        Berechnet die Summe der Differenzen der Häufigkeiten von Spiegelpaaren.

        :type s: str
        :rtype: int
        """
        # Häufigkeit aller Zeichen im String zählen
        freq = Counter(s)
        total_diff = 0

        # Definition der Buchstaben-Paare (a-z)
        # Wir iterieren nur über die erste Hälfte des Alphabets (Index 0-12)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(13):
            char_c = alphabet[i]
            char_m = alphabet[25 - i]
            total_diff += abs(freq[char_c] - freq[char_m])

        # Definition der Ziffern-Paare (0-9)
        # Wir iterieren nur über die erste Hälfte der Ziffern (Index 0-4)
        digits = "0123456789"
        for i in range(5):
            char_c = digits[i]
            char_m = digits[9 - i]
            total_diff += abs(freq[char_c] - freq[char_m])

        return total_diff

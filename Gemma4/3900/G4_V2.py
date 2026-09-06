"""
Dieses Modul enthält die Lösung zur Berechnung der maximalen Länge
eines balancierten Teilstrings unter Verwendung von maximal einem Swap.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Bietet Funktionen zur Analyse von binären Strings, um die maximale
    Länge eines balancierten Teilstrings zu ermitteln.
    """

    # pylint: disable=invalid-name
    def longestBalanced(self, s):
        """
        Berechnet die maximale Länge eines Teilstrings mit gleicher Anzahl
        an '0'en und '1'en, nachdem maximal ein Zeichen-Swap durchgeführt wurde.

        :type s: str
        :rtype: int
        """
        # Zähle die Vorkommen beider Zeichen im gesamten String.
        # Zeitkomplexität: O(n), wobei n die Länge des Strings s ist.
        count_zeros = s.count('0')
        count_ones = s.count('1')

        # Ein Teilstring ist balanciert, wenn er k Nullen und k Einsen enthält.
        # Die maximale Anzahl an Paaren, die wir überhaupt bilden können,
        # ist durch das seltener vorkommende Zeichen limitiert.
        # Da ein einziger Swap es erlaubt, ein benötigtes Zeichen von einer
        # beliebigen Stelle des Strings in das gewünschte Fenster zu verschieben,
        # können wir immer ein optimales Fenster der Größe 2 * min(0s, 1s) erreichen.
        max_pairs = min(count_zeros, count_ones)

        return 2 * max_pairs

"""
Dieses Modul bietet eine Lösung zur Gewichtung von Wörtern und deren
Mapping auf Zeichen in umgekehrter alphabetischer Reihenfolge.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Berechnung von Wortgewichten basierend auf einem
    gegebenen Alphabet-Gewichtungs-Array.
    """

    def mapWordWeights(self, words, weights): # pylint: disable=invalid-name
        """
        Berechnet das Gesamtgewicht jedes Wortes, wendet Modulo 26 an
        und mappt das Ergebnis auf einen Buchstaben (0 -> 'z', 25 -> 'a').

        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []

        for word in words:
            # 1. Berechne das Gesamtgewicht des Wortes
            word_weight = 0
            for char in word:
                # Ermittle den Index des Buchstabens (a=0, b=1, ..., z=25)
                index = ord(char) - ord('a')
                word_weight += weights[index]

            # 2. Berechne das Gewicht modulo 26
            mod_val = word_weight % 26

            # 3. Mapping in umgekehrter alphabetischer Reihenfolge:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped_char = chr(ord('z') - mod_val)
            result.append(mapped_char)

        # Verbinde alle Zeichen zu einem finalen String
        return "".join(result)

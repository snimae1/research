"""
Dieses Modul implementiert eine Lösung zur Berechnung des maximalen Scores,
der durch die Auswahl von k geordneten Paaren aus zwei Arrays erzielt werden kann.
"""
import functools


class Solution:
    """
    Klasse zur Lösung des Problems der maximalen Score-Optimierung.
    Nutzt dynamische Programmierung mit Memoization.
    """

    # pylint: disable=too-few-public-methods
    def maxScore(self, nums1, nums2, k):
        """
        Berechnet den maximalen Gesamtwert aus k Paaren von Indizes.

        :param nums1: Liste von Ganzzahlen (n Elemente)
        :param nums2: Liste von Ganzzahlen (m Elemente)
        :param k: Anzahl der zu wählenden Paare
        :return: Maximaler erreichbarer Score
        """
        # pylint: disable=invalid-name
        n = len(nums1)
        m = len(nums2)

        @functools.lru_cache(None)
        def solve(i, j, p):
            """
            Rekursive Hilfsfunktion zur Berechnung des optimalen Scores.

            Args:
                i (int): Aktueller Index in nums1
                j (int): Aktueller Index in nums2
                p (int): Verbleibende Anzahl an benötigten Paaren
            Returns:
                int: Maximaler Score für den aktuellen Zustand
            """
            # Basisfall: Alle benötigten k Paare wurden erfolgreich gewählt
            if p == 0:
                return 0

            # Basisfall: Ende einer Liste erreicht, bevor k Paare gebildet wurden.
            # Wir nutzen einen sehr kleinen Wert, um diesen Pfad als ungültig zu markieren.
            if i == n or j == m:
                return float('-inf')

            # Option 1: Aktuelle Elemente nums1[i] und nums2[j] als Paar wählen.
            # Wir addieren das Produkt und bewegen uns in beiden Listen und im
            # Zähler p einen Schritt weiter.
            res_pair = (nums1[i] * nums2[j]) + solve(i + 1, j + 1, p - 1)

            # Option 2: Das aktuelle Element von nums1 überspringen.
            res_skip_i = solve(i + 1, j, p)

            # Option 3: Das aktuelle Element von nums2 überspringen.
            res_skip_j = solve(i, j + 1, p)

            # Rückgabe des Maximums aus den drei möglichen Entscheidungen
            return max(res_pair, res_skip_i, res_skip_j)

        return solve(0, 0, k)

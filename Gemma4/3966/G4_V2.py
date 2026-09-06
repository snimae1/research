"""
Modul zur Berechnung von 'guten' Ganzzahlen in einem bestimmten Bereich.
Eine Zahl ist 'gut', wenn die absolute Differenz zwischen benachbarten Ziffern maximal k ist.
"""

from functools import lru_cache


class Solution:
    """
    Bietet eine Methode, um die Anzahl der 'guten' Zahlen im Intervall [l, r] zu finden.
    """

    # pylint: disable=too-few-public-methods
    def good_integers(self, l, r, k):
        """
        Berechnet die Anzahl der Zahlen zwischen l und r, bei denen die Differenz
        zwischen allen benachbarten Ziffern höchstens k beträgt.

        :param l: Untergrenze des Bereichs (int)
        :param r: Obergrenze des Bereichs (int)
        :param k: Maximal erlaubte absolute Differenz (int)
        :return: Anzahl der gültigen Zahlen (int)
        """

        def count_good(n_str, k_val):
            """
            Hilfsfunktion, die mittels Digit-DP die guten Zahlen von 0 bis n_str zählt.
            """
            @lru_cache(None)
            def dp(idx, prev_digit, is_less, is_started):
                # Basisfall: Wir haben alle Stellen der Zahl erfolgreich durchlaufen
                if idx == len(n_str):
                    return 1

                res = 0
                # Bestimme die Obergrenze für die aktuelle Ziffer an Position idx
                limit = int(n_str[idx]) if not is_less else 9

                for d in range(limit + 1):
                    # Prüfen, ob wir uns bereits unter der Obergrenze der Zielzahl befinden
                    next_is_less = is_less or (d < limit)

                    if not is_started:
                        # Phase der führenden Nullen
                        if d == 0:
                            # Wir setzen eine führende Null, die Zählung beginnt noch nicht
                            res += dp(idx + 1, -1, next_is_less, False)
                        else:
                            # Die erste signifikante Ziffer wurde gesetzt
                            res += dp(idx + 1, d, next_is_less, True)
                    else:
                        # Prüfe die Bedingung: Differenz zur vorherigen Ziffer <= k
                        if abs(d - prev_digit) <= k_val:
                            res += dp(idx + 1, d, next_is_less, True)

                return res

            return dp(0, -1, False, False)

        # Das Ergebnis für den Bereich [l, r] ist die Differenz
        # der Mengen [0, r] und [0, l-1].
        return count_good(str(r), k) - count_good(str(l - 1), k)

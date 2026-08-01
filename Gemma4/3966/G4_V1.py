from functools import lru_cache

class Solution(object):

    def goodIntegers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        
        def count_good(n_str, k):
            # Memoization zur Speicherung von Zwischenergebnissen: 
            # (index der Ziffer, vorherige Ziffer, ist_kleiner, hat_begonnen)
            @lru_cache(None)
            def dp(idx, prev_digit, is_less, is_started):
                # Basisfall: Wir haben alle Stellen der Zahl durchlaufen
                if idx == len(n_str):
                    return 1
                
                res = 0
                # Bestimme die Obergrenze für die aktuelle Ziffer
                # Wenn 'is_less' True ist, können wir jede Ziffer von 0-9 nehmen.
                # Andernfalls sind wir durch die Ziffer an der aktuellen Position in n_str begrenzt.
                limit = int(n_str[idx]) if not is_less else 9
                
                for d in range(limit + 1):
                    # Neue Zustände berechnen
                    next_is_less = is_less or (d < limit)
                    
                    if not is_started:
                        # Wir befinden uns noch in der Phase der führenden Nullen
                        if d == 0:
                            # Ziffer ist 0 und wir haben noch nicht "richtig" angefangen
                            res += dp(idx + 1, -1, next_is_less, False)
                        else:
                            # Die erste signifikante (nicht-null) Ziffer wird gesetzt
                            res += dp(idx + 1, d, next_is_less, True)
                    else:
                        # Wir haben bereits mit der Zahl begonnen, also prüfen wir die Bedingung |a - b| <= k
                        if abs(d - prev_digit) <= k:
                            res += dp(idx + 1, d, next_is_less, True)
                
                return res

            # Start des DP-Prozesses
            # idx=0, prev=-1, is_less=False, is_started=False
            return dp(0, -1, False, False)

        # Das Ergebnis für den Bereich [l, r] ist: count(r) - count(l-1)
        # Wir übergeben die Zahlen als Strings an die Hilfsfunktion
        return count_good(str(r), k) - count_good(str(l - 1), k)

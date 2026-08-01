class Solution(object):

    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        # Konvertiere die Zahl und die Ziffer in Strings für den Vergleich
        s_n = str(n)
        s_x = str(x)

        # Bedingung 1: Enthält mindestens ein Vorkommen der Ziffer x
        contains_x = s_x in s_n
        
        # Bedingung 2: Startet NICHT mit der Ziffer x
        # s_n[0] gibt das erste Zeichen des Strings zurück
        does_not_start_with_x = s_n[0] != s_x

        # Beide Bedingungen müssen wahr sein (UND-Verknüpfung)
        return contains_x and does_not_start_with_x

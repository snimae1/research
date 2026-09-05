"""Lösung für die Berechnung der Anzahl verwendeter Kommas."""


class Solution(object):
    """Berechnet die Anzahl der Kommas für alle Zahlen von 1 bis n."""

    def countCommas(self, n):
        """
        Berechnet die Gesamtzahl der verwendeten Kommas.

        :param n: Obere Grenze des Zahlenbereichs.
        :type n: int
        :return: Anzahl aller Kommas von 1 bis n.
        :rtype: int
        """

        # Erst ab 1.000 wird ein Komma benötigt.
        if n < 1000:
            return 0

        # Jede Zahl von 1.000 bis n enthält genau ein Komma.
        return n - 999

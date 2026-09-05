"""Lösung zur Berechnung der insgesamt verwendeten Kommas."""

# pylint: disable=invalid-name,too-few-public-methods
class Solution(object):
    """Berechnet die Anzahl der Kommas in Zahlen von 1 bis n."""

    def countCommas(self, n):
        """
        Berechnet die Gesamtzahl der verwendeten Kommas.

        :param n: Obere Grenze des Zahlenbereichs.
        :type n: int
        :return: Anzahl aller verwendeten Kommas.
        :rtype: int
        """
        total_commas = 0
        comma_threshold = 1000

        while comma_threshold <= n:
            # Jede Zahl ab dieser Grenze erhält ein zusätzliches Komma.
            total_commas += n - comma_threshold + 1
            comma_threshold *= 1000

        return total_commas

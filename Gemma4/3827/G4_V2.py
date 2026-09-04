"""
Dieses Modul bietet eine Lösung zur Zählung von Monobit-Zahlen
im Bereich von 0 bis n.
"""


class Solution:
    """
    Klasse zur Berechnung der Anzahl von Monobit-Integern.
    Ein Integer gilt als Monobit, wenn alle Bits seiner Binärdarstellung identisch sind.
    """

    def count_monobit(self, n):
        """
        Zählt die Monobit-Zahlen im Bereich [0, n].

        :type n: int
        :rtype: int
        :return: Anzahl der Monobit-Zahlen als Integer
        """
        # Wir beginnen mit 1, da die Zahl 0 (binär "0") immer als Monobit gilt.
        count = 1

        # Ein Monobit-Integer (außer 0) besteht aus einer Kette von Einsen.
        # Diese Zahlen folgen dem Muster: (2^k - 1) -> 1, 3, 7, 15...
        k = 1
        while True:
            monobit_value = (2**k) - 1
            if monobit_value <= n:
                count += 1
                k += 1
            else:
                break

        return count

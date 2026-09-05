```python
"""Berechnet die Summe aller möglichen k-stelligen Zahlen."""

class Solution:
    """Lösung für die Berechnung der Summe möglicher Zahlen."""

    def sumOfNumbers(self, l, r, k):
        """
        Berechnet die Summe aller Zahlen mit k Ziffern aus [l, r].

        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        mod = 10**9 + 7

        # Anzahl der möglichen Ziffern und ihre Gesamtsumme.
        digit_count = r - l + 1
        digit_sum = (l + r) * digit_count // 2

        # Jede mögliche Ziffer steht an jeder Stelle gleich oft.
        combinations = pow(digit_count, k - 1, mod)

        # Summe der Stellenwerte: 1 + 10 + ... + 10^(k-1).
        repunit = (pow(10, k, mod) - 1) * pow(9, mod - 2, mod) % mod

        return digit_sum * combinations % mod * repunit % mod
```

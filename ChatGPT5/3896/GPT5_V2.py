"""Lösung für das Alternating-Prime-Array-Problem."""

class Solution:  # pylint: disable=too-few-public-methods
"""Berechnet die minimale Anzahl benötigter Inkrement-Operationen."""

```
def minOperations(self, nums):  # pylint: disable=invalid-name
    """
    Transformiert nums mit minimal vielen Inkrementen in ein
    alternating-prime Array.

    Gerade Indizes müssen Primzahlen enthalten, ungerade Indizes
    müssen nicht-prime Zahlen enthalten.

    :type nums: List[int]
    :rtype: int
    """
    limit = max(nums) + 300
    is_prime = self._create_prime_table(limit)
    next_prime = self._create_next_prime_table(is_prime)

    operations = 0

    for index, number in enumerate(nums):
        if index % 2 == 0:
            operations += next_prime[number] - number
        elif is_prime[number]:
            operations += 1

    return operations

@staticmethod
def _create_prime_table(limit):
    """Erstellt mit dem Sieb des Eratosthenes eine Primzahltabelle."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    divisor = 2
    while divisor * divisor <= limit:
        if is_prime[divisor]:
            for multiple in range(divisor * divisor, limit + 1, divisor):
                is_prime[multiple] = False
        divisor += 1

    return is_prime

@staticmethod
def _create_next_prime_table(is_prime):
    """Bestimmt für jede Zahl die kleinste Primzahl, die mindestens so groß ist."""
    next_prime = [0] * len(is_prime)
    nearest_prime = -1

    for number in range(len(is_prime) - 1, -1, -1):
        if is_prime[number]:
            nearest_prime = number
        next_prime[number] = nearest_prime

    return next_prime
```

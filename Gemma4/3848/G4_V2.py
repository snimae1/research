"""
Dieses Modul bietet eine Lösung zur Überprüfung von Digitorial-Permutationen.
Eine Zahl heißt Digitorial-Permutation, wenn die Summe der Fakultäten ihrer 
Ziffern eine Permutation der ursprünglichen Ziffern ergibt.
"""

import math


class Solution:
    """
    Klasse zur Analyse von Zahlen auf ihre Digitorial-Eigenschaften.
    """

    def calculate_factorial_sum(self, n: int) -> int:
        """
        Berechnet die Summe der Fakultäten aller Ziffern einer Zahl.

        Args:
            n (int): Die zu prüfende Zahl.

        Returns:
            int: Die Summe der Fakultäten der Ziffern.
        """
        return sum(math.factorial(int(digit)) for digit in str(n))

    def is_digitorial_permutation(self, n: int) -> bool:
        """
        Prüft, ob eine Zahl eine Digitorial-Permutation ist.

        Eine Zahl ist eine Digitorial-Permutation, wenn die Summe der
        Fakultäten ihrer Ziffern dieselben Ziffern enthält wie die 
        Ursprungszahl (unabhängig von der Reihenfolge).

        Args:
            n (int): Die zu prüfende Zahl.

        Returns:
            bool: True, wenn es eine Digitorial-Permutation ist, sonst False.
        """
        factorial_sum = self.calculate_factorial_sum(n)
        
        # Vergleich der sortierten Ziffern beider Zahlen, 
        # um eine Permutation festzustellen.
        return sorted(str(n)) == sorted(str(factorial_sum))

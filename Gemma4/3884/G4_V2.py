"""
Dieses Modul enthält die Klasse Solution, welche eine Methode zur
Suche des ersten passenden Index in einem String bereitstellt.
"""

class Solution:
    """
    Bietet eine Lösung zur Identifizierung des kleinsten Index i,
    bei dem s[i] gleich s[n - i - 1] ist.
    """

    def first_matching_index(self, s):
        """
        Findet den kleinsten Index i, sodass das Zeichen an Position i
        mit dem Zeichen an der spiegelbildlichen Position übereinstimmt.

        :type s: str
        :rtype: int
        """
        n = len(s)

        # Wir iterieren von i = 0 bis n-1, um den kleinstmöglichen Index zu finden
        for i in range(n):
            # Überprüfung der Bedingung: s[i] muss gleich s[n - i - 1] sein
            if s[i] == s[n - i - 1]:
                return i

        # Wenn die Schleife komplett durchläuft, ohne ein Match zu finden,
        # geben wir -1 zurück.
        return -1

# pylint: disable=too-few-public-methods

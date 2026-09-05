"""
Dieses Modul enthält eine Lösung zur Berechnung der minimalen Anzahl 
von Operationen, um einen String durch Teilstring-Sortierung zu sortieren.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Lösung des Problems 'Minimum Operations to Sort a String'.
    """

    def min_operations(self, s):
        """
        Berechnet die minimale Anzahl an Operationen, um s sortiert zu machen.

        :type s: str
        :rtype: int
        """
        # Schritt 1: Prüfen, ob der String bereits sortiert ist
        if list(s) == sorted(s):
            return 0

        n = len(s)
        min_char = min(s)
        max_char = max(s)

        # Schritt 2: Prüfung auf 1 Operation.
        # Eine Operation reicht aus, wenn entweder das erste Zeichen bereits 
        # das globale Minimum ist oder das letzte Zeichen das globale Maximum.
        if s[0] == min_char or s[n-1] == max_char:
            return 1

        # Schritt 3: Prüfung auf Unmöglichkeit.
        # Wenn das Maximum am Anfang UND das Minimum am Ende steht,
        # kann keine Teilstring-Operation (die nicht den ganzen String umfasst)
        # beide Zeichen an die richtige Position bringen.
        if s[0] == max_char and s[n-1] == min_char:
            return -1

        # Schritt 4: In allen anderen Fällen sind genau 2 Operationen nötig.
        return 2

"""
Dieses Modul berechnet die Punktedifferenz zwischen zwei Spielern basierend auf
spezifischen Rollenwechsel-Regeln in einer Spielserie.
"""

class Solution:
    """
    Enthält die Logik zur Berechnung der Differenz der Endstände
    von zwei Spielern.
    """

    def score_difference(self, nums):
        """
        Berechnet die Differenz (Spieler 1 - Spieler 2) basierend auf den Spielregeln.

        :type nums: List[int]
        :rtype: int
        """
        # Initialisierung: Spieler 1 ist aktiv (True = Spieler 1, False = Spieler 2)
        player1_active = True
        score1 = 0
        score2 = 0

        # Nutzung von enumerate für bessere Lesbarkeit und Pylint-Konformität
        for i, points in enumerate(nums):
            # Regel 1: Wenn die Punkte ungerade sind, tauschen die Spieler ihre Rollen
            if points % 2 != 0:
                player1_active = not player1_active

            # Regel 2: Jedes 6. Spiel (Index 5, 11, 17...) tauschen die Spieler ihre Rollen
            # i + 1 wird verwendet, um die 1-basierte Spielnummer zu erhalten
            if (i + 1) % 6 == 0:
                player1_active = not player1_active

            # Regel 3: Der aktive Spieler erhält die Punkte des Spiels
            if player1_active:
                score1 += points
            else:
                score2 += points

        return score1 - score2

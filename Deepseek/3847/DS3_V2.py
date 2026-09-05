"""
Modul zur Berechnung der Punktedifferenz zwischen zwei Spielern.
"""

class Solution:  # Python‑3‑Vererbung von object ist nicht nötig
    """
    Lösungsansatz für die gegebene Aufgabenstellung.
    """

    # Die Methode muss genau diesen Namen haben (laut Aufgabenstellung).
    # pylint: disable=invalid-name
    def scoreDifference(self, nums):
        """
        Berechnet die Differenz der Punktestände von Spieler 1 und Spieler 2.

        :param nums: Liste der Punktzahlen pro Spiel
        :type nums: List[int]
        :return: Punktedifferenz (Spieler1 - Spieler2)
        :rtype: int
        """
        active = 0          # 0 → Spieler 1 aktiv, 1 → Spieler 2 aktiv
        score1 = 0
        score2 = 0

        for i, points in enumerate(nums):
            # Regel 1: Bei ungerader Punktzahl wechseln die Rollen
            if points % 2 == 1:
                active = 1 - active

            # Regel 2: Jedes 6. Spiel (Indizes 5, 11, 17, …) erneuter Tausch
            if i % 6 == 5:
                active = 1 - active

            # Aktiver Spieler erhält die Punkte
            if active == 0:
                score1 += points
            else:
                score2 += points

        return score1 - score2

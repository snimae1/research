class Solution(object):

    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        # Initialisierung: Spieler 1 ist aktiv (True = Spieler 1, False = Spieler 2)
        player1_active = True
        score1 = 0
        score2 = 0

        for i in range(len(nums)):
            points = nums[i]

            # Regel 1: Wenn die Punkte ungerade sind, tauschen die Spieler ihre Rollen
            if points % 2 != 0:
                player1_active = not player1_active

            # Regel 2: Jedes 6. Spiel (Index 5, 11, 17...) tauschen die Spieler ihre Rollen
            # Wir prüfen auf (i + 1), da das erste Spiel bei Index 0 beginnt
            if (i + 1) % 6 == 0:
                player1_active = not player1_active

            # Regel 3: Der aktive Spieler erhält die Punkte des Spiels
            if player1_active:
                score1 += points
            else:
                score2 += points

        # Rückgabe der Differenz (Spieler 1 minus Spieler 2)
        return score1 - score2


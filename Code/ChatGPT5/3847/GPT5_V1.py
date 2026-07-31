class Solution(object):
    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0

        # True = erster Spieler ist aktiv
        first_active = True

        for i, points in enumerate(nums):
            # Tausch bei ungerader Punktzahl
            if points % 2 == 1:
                first_active = not first_active

            # Tausch in jedem 6. Spiel (Index 5, 11, 17, ...)
            if (i + 1) % 6 == 0:
                first_active = not first_active

            # Aktiver Spieler erhält die Punkte
            if first_active:
                first += points
            else:
                second += points

        return first - second

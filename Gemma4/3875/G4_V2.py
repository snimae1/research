"""
Dieses Modul enthält die Lösung für das Problem der Konstruktion eines
uniformen Arrays (alle Elemente entweder gerade oder ungerade).
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Bietet eine Methode, um zu prüfen, ob ein Array durch spezifische
    Subtraktionsregeln in ein uniformes Array (nur gerade oder nur ungerade)
    umgewandelt werden kann.
    """

    # pylint: disable=invalid-name
    def uniformArray(self, nums1):
        """
        Bestimmt, ob nums2 so konstruiert werden kann, dass alle Elemente
        entweder gerade oder ungerade sind.

        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)
        # Zähle die Anzahl der ungeraden Zahlen im ursprünglichen Array
        num_odds = sum(1 for x in nums1 if x % 2 != 0)

        # Ziel: Alle Elemente in nums2 entweder gerade oder alle ungerade.

        # FALL 1: Kann man nums2 komplett GERADE machen?
        # Gerade Zahlen bleiben gerade.
        # Ungerade Zahlen werden gerade, wenn man eine andere ungerade Zahl abzieht.
        # Das ist möglich, wenn es keine oder mindestens zwei ungerade Zahlen gibt.
        can_be_all_even = num_odds == 0 or num_odds >= 2

        # FALL 2: Kann man nums2 komplett UNGERADE machen?
        # Ungerade Zahlen bleiben ungerade.
        # Gerade Zahlen werden ungerade, wenn man eine ungerade Zahl abzieht.
        # Das ist möglich, wenn mindestens eine ungerade Zahl existiert.
        can_be_all_odd = num_odds >= 1

        # Sonderfall: Ein Array mit nur einem Element ist per Definition uniform.
        if n == 1:
            return True

        return can_be_all_even or can_be_all_odd

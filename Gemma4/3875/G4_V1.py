class Solution(object):

    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """ 
        n = len(nums1)
        # Zähle, wie viele odd (ungerade) Zahlen im Array sind
        odds = [x for x in nums1 if x % 2 != 0]
        num_odds = len(odds)
        num_evens = n - num_odds

        # Ziel: Alle Elemente in nums2 entweder gerade oder alle ungerade.

        # FALL 1: Kann man nums2 komplett GERADE machen?
        # - Wenn eine Zahl bereits gerade ist, nehmen wir nums2[i] = nums1[i]. (OK)
        # - Wenn eine Zahl ungerade ist, müssen wir eine andere ungerade Zahl 
        #   abziehen (ungerade - ungerade = gerade).
        # Das ist möglich, wenn es entweder gar keine ungeraden Zahlen gibt 
        # oder mindestens zwei, damit jede ungerade Zahl einen Partner zum Abziehen hat.
        can_be_all_even = (num_odds == 0) or (num_odds >= 2)

        # FALL 2: Kann man nums2 komplett UNGERADE machen?
        # - Wenn eine Zahl bereits ungerade ist, nehmen wir nums2[i] = nums1[i]. (OK)
        # - Wenn eine Zahl gerade ist, müssen wir eine ungerade Zahl abziehen 
        #   (gerade - ungerade = ungerade).
        # Das ist möglich, wenn mindestens eine ungerade Zahl im Array existiert.
        # Falls das Array nur aus geraden Zahlen besteht (num_odds == 0), 
        # kann man keine einzige Zahl ungerade machen.
        can_be_all_odd = (num_odds >= 1)

        # Sonderfall: Wenn n=1, ist das Array per Definition immer uniform,
        # egal ob die eine Zahl gerade oder ungerade ist.
        if n == 1:
            return True

        # Wir geben true zurück, wenn mindestens einer der beiden Fälle möglich ist.
        return can_be_all_even or can_be_all_odd

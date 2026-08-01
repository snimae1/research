class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_odd = None

        # Kleinste ungerade Zahl bestimmen
        for x in nums1:
            if x % 2 == 1:
                if min_odd is None or x < min_odd:
                    min_odd = x

        # Prüft, ob alle Zahlen auf die Zielparität gebracht werden können.
        # target = 0 -> alle gerade
        # target = 1 -> alle ungerade
        def can_make(target):
            for x in nums1:
                if x % 2 != target:
                    # Parität muss geändert werden.
                    # Das ist nur möglich, wenn es eine kleinere ungerade Zahl gibt.
                    if min_odd is None or min_odd >= x:
                        return False
            return True

        return can_make(0) or can_make(1)

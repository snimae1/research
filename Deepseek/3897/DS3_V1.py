class Solution(object):
    def maxValue(self, nums1, nums0):
        """
        :type nums1: List[int]
        :type nums0: List[int]
        :rtype: int
        """
        MOD = 1_000_000_007
        n = len(nums1)

        # Hilfsklasse, die ein Segment repräsentiert und einen Vergleichsoperator
        # bereitstellt, der die optimale Reihenfolge für maximale Verkettung liefert.
        class Segment:
            __slots__ = ('val', 'length', 'val_mod')

            def __init__(self, val, length, val_mod):
                self.val = val          # ganzzahliger Wert des Binärsegments (BigInt)
                self.length = length    # Länge in Bits
                self.val_mod = val_mod  # Wert modulo MOD

            def __lt__(self, other):
                # self soll vor other einsortiert werden, falls
                # self + other > other + self (im Sinne der Binärverkettung).
                left = (self.val << other.length) + other.val
                right = (other.val << self.length) + self.val
                return left > right

        segments = []
        for i in range(n):
            ones = nums1[i]
            zeros = nums0[i]
            length = ones + zeros
            # val = (2^ones - 1) * 2^zeros
            val = ((1 << ones) - 1) << zeros
            val_mod = val % MOD
            segments.append(Segment(val, length, val_mod))

        # Sortieren mit dem angepassten Vergleichsoperator
        segments.sort()

        # Verkettung modulo MOD berechnen
        res = 0
        for seg in segments:
            # res = res * 2^length + val
            res = (res * pow(2, seg.length, MOD) + seg.val_mod) % MOD

        return res

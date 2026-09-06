"""
Lösung für das Problem: Maximale binäre Verkettung von Segmenten.

Gegeben zwei Arrays nums1 und nums0, die die Anzahl der Einsen bzw. Nullen
in Segmenten beschreiben. Die Segmente können beliebig umsortiert werden,
um die größtmögliche Binärzahl durch Verkettung zu erhalten.
"""
# pylint: disable=invalid-name, too-few-public-methods

class Solution:
    """
    Enthält die Methode maxValue zur Berechnung des maximalen Wertes.
    """
    def maxValue(self, nums1, nums0):
        """
        Berechnet den maximalen ganzzahligen Wert der verketteten Binärzeichenkette.

        :param nums1: Liste mit der Anzahl der Einsen je Segment.
        :param nums0: Liste mit der Anzahl der Nullen je Segment.
        :return: Maximaler Wert modulo 10^9 + 7.
        """
        MOD = 1_000_000_007
        n = len(nums1)

        class Segment:
            """
            Repräsentiert ein binäres Segment mit Vergleichslogik für
            optimale Sortierung bei der Verkettung.
            """
            __slots__ = ('value', 'length', 'value_mod')

            def __init__(self, value, length, value_mod):
                self.value = value          # ganzzahliger Wert des Binärsegments
                self.length = length        # Länge in Bits
                self.value_mod = value_mod  # Wert modulo MOD

            def __lt__(self, other):
                """
                Sortierkriterium: self soll vor other stehen, wenn
                self + other > other + self (als Binärzahlen interpretiert).
                """
                left = (self.value << other.length) + other.value
                right = (other.value << self.length) + self.value
                return left > right

        # Segmente aufbauen
        segments = []
        for i in range(n):
            ones = nums1[i]
            zeros = nums0[i]
            length = ones + zeros
            # Binärwert des Segments: (2^ones - 1) << zeros
            value = ((1 << ones) - 1) << zeros
            value_mod = value % MOD
            segments.append(Segment(value, length, value_mod))

        # Segmente nach optimalem Verkettungskriterium sortieren
        segments.sort()

        # Verkettung modulo MOD durchführen
        result = 0
        for seg in segments:
            # result = result * 2^length + segment.value
            result = (result * pow(2, seg.length, MOD) + seg.value_mod) % MOD

        return result

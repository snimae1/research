"""
Dieses Modul bietet eine Lösung, um die minimale Länge eines zu entfernenden
Präfixes aus einem Integer-Array zu berechnen, sodass der Rest strikt steigend ist.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Berechnung der minimalen Präfixlänge.
    """

    # pylint: disable=invalid-name
    def minimumPrefixLength(self, nums):
        """
        Berechnet die minimale Länge des zu entfernenden Präfixes,
        damit das verbleibende Array strikt steigend ist.

        :type nums: List[int]
        :rtype: int
        """
        # Die Länge des Arrays ermitteln
        array_length = len(nums)

        # Wir untersuchen das Array von hinten nach vorne, um den längsten
        # strikt steigenden Suffix zu finden.
        # Wir starten beim vorletzten Element (Index n-2).
        index = array_length - 2

        # Solange das aktuelle Element kleiner ist als sein rechter Nachbar,
        # ist die Bedingung 'strikt steigend' erfüllt.
        while index >= 0 and nums[index] < nums[index + 1]:
            index -= 1

        # Wenn die Schleife stoppt, ist 'index' die Position des ersten Elements,
        # das die steigende Reihenfolge bricht.
        # Da die Indizes bei 0 beginnen, ist die Anzahl der zu entfernenden
        # Elemente (das Präfix) genau index + 1.
        return index + 1


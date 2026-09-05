"""Lösung für die Aufgabe 'First Unique Frequency'."""

# pylint: disable=invalid-name
# Der Klassenname und der Methodenname sind durch die Aufgabenstellung vorgegeben.
class Solution:
    """Löst die Aufgabe zur Suche nach der ersten eindeutigen Häufigkeit."""

    # pylint: disable=invalid-name
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Speichert, wie oft jede Zahl im Array vorkommt.
        frequencies = {}
        for number in nums:
            frequencies[number] = frequencies.get(number, 0) + 1

        # Speichert, wie viele verschiedene Zahlen dieselbe Häufigkeit haben.
        frequency_counts = {}
        for frequency in frequencies.values():
            frequency_counts[frequency] = (
                frequency_counts.get(frequency, 0) + 1
            )

        # Das Array von links nach rechts durchsuchen.
        # Das erste Element mit einer eindeutigen Häufigkeit wird zurückgegeben.
        for number in nums:
            frequency = frequencies[number]

            if frequency_counts[frequency] == 1:
                return number

        # Keine Zahl besitzt eine eindeutige Häufigkeit.
        return -1

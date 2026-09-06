"""
Dieses Modul bietet eine Lösung zur Berechnung und zum Vergleich
der Summen des aufsteigenden und absteigenden Teils eines bitonischen Arrays.
"""

class Solution:
    """
    Klasse zur Analyse von bitonischen Arrays.
    """

    def compare_bitonic_sums(self, nums):
        """
        Vergleicht die Summe des aufsteigenden Teils mit der Summe des absteigenden Teils.

        :type nums: List[int]
        :rtype: int
        """
        # Suche nach dem peak_index
        # Ein bitonisches Array steigt strikt an und fällt dann strikt ab.
        peak_index = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                peak_index = i + 1
            else:
                break

        # Berechnung der Summen
        # Slicing wird verwendet, um die Teile zu trennen (Peak gehört zu beiden)
        ascending_sum = sum(nums[:peak_index + 1])
        descending_sum = sum(nums[peak_index:])

        # Vergleich der Summen entsprechend der Aufgabenstellung:
        # Return 0 if ascending > descending
        if ascending_sum > descending_sum:
            return 0

        # Return 1 if descending > ascending
        if descending_sum > ascending_sum:
            return 1

        # Return -1 if both are equal
        return -1

"""
Modul zur Lösung des Problems der Verschmelzung benachbarter identischer Elemente.
Dieses Modul implementiert eine effiziente Stack-basierte Lösung.
"""

class Solution:
    """
    Bietet eine Methode, um ein Array von Integern so zu reduzieren, dass 
    benachbarte identische Elemente zu ihrer Summe verschmolzen werden.
    """

    def merge_adjacent(self, nums):
        """
        Verschmilzt benachbarte gleiche Elemente wiederholt, bis keine
        weiteren Änderungen möglich sind.

        :type nums: List[int]
        :rtype: List[int]
        """
        # Ein Stack wird verwendet, um die Elemente linear zu verarbeiten
        # und sofort auf das letzte Element für einen möglichen Merge zuzugreifen.
        stack = []

        for num in nums:
            current_val = num

            # Prüfe, ob das aktuelle Element mit dem letzten Element im Stack identisch ist.
            # Falls ja, verschmelze sie und prüfe rekursiv/iterativ den neuen Wert.
            while stack and stack[-1] == current_val:
                current_val += stack.pop()

            stack.append(current_val)

        return stack

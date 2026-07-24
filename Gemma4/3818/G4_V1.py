class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Wir starten am Ende des Arrays und gehen rückwärts.
        # n ist die Länge des Arrays.
        n = len(nums)
        
        # Wir prüfen ab dem vorletzten Element, ob es kleiner 
        # als das Element rechts daneben ist.
        i = n - 2
        while i >= 0 and nums[i] < nums[i+1]:
            i -= 1
            
        # i ist nun der Index des letzten Elements, das die 'strikt steigende' 
        # Bedingung bricht (oder -1, wenn das ganze Array steigt).
        # Die Länge des Präfixes, das entfernt werden muss, entspricht
        # genau dem Index i + 1.
        return i + 1

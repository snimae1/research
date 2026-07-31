class Solution(object):

    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Ein Dictionary, um die Häufigkeit jeder Zahl zu speichern
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # Wir gehen das Array ein zweites Mal durch, um die Reihenfolge (Index) 
        # beizubehalten und den ersten Treffer zu finden
        for num in nums:
            # Prüfung: Ist die Zahl gerade UND kommt sie genau einmal vor?
            if num % 2 == 0 and counts[num] == 1:
                return num
        
        # Wenn keine solche Zahl gefunden wurde, geben wir -1 zurück
        return -1

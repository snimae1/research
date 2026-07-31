from collections import Counter

class Solution(object):
    def minDistinctFreqPair(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. Frequenzen aller Zahlen zählen
        # Beispiel: [1,1,2,2,3,4] -> {1: 2, 2: 2, 3: 1, 4: 1}
        counts = Counter(nums)
        
        # 2. Die eindeutigen Zahlen sortiert extrahieren
        # Das stellt sicher, dass wir zuerst die kleinstmöglichen x und y prüfen.
        unique_elements = sorted(counts.keys())
        
        # 3. Alle Paare (x, y) prüfen wobei x < y
        # Durch die verschachtelten Schleifen über die sortierte Liste 
        # finden wir automatisch das Paar mit dem kleinsten x und dann dem kleinsten y.
        for i in range(len(unique_elements)):
            x = unique_elements[i]
            for j in range(i + 1, len(unique_elements)):
                y = unique_elements[j]
                
                # Bedingung: Die Frequenzen müssen unterschiedlich sein
                if counts[x] != counts[y]:
                    return [x, y]
        
        # 4. Wenn keine gültigen Paare gefunden wurden
        return [-1, -1]

class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Anzahl der dominanten Indizes
        dominant_count = 0
        # Summe aller Elemente rechts vom aktuellen Index
        right_sum = 0
        # Anzahl der Elemente rechts vom aktuellen Index
        right_count = 0
        
        # Wir iterieren von rechts nach links (vom letzten Element zum ersten)
        for i in range(len(nums) - 1, -1, -1):
            current_val = nums[i]
            
            # Bedingung: Das rechteste Element ist nie dominant.
            # Daher prüfen wir nur, wenn rechts bereits Elemente existieren (right_count > 0).
            if right_count > 0:
                average = right_sum / float(right_count)
                if current_val > average:
                    dominant_count += 1
            
            # Aktualisiere Summe und Anzahl für das nächste Element (das links davon liegt)
            right_sum += current_val
            right_count += 1
            
        return dominant_count

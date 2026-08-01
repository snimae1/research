class Solution(object):

    def countGoodSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_good = 0
        # current_ors speichert Paare von (or_wert, start_index).
        # Es repräsentiert alle distinkten Bitwise-OR Werte von Subarrays, die am aktuellen Index enden.
        current_ors = [] 
        # last_pos speichert die letzte Position, an der ein bestimmter Wert im Array vorkam.
        last_pos = {} 
        
        for i in range(len(nums)):
            val = nums[i]
            last_pos[val] = i
            
            # 1. Aktualisiere die OR-Werte für alle Subarrays, die am aktuellen Index i enden.
            next_ors = []
            for v, idx in current_ors:
                new_v = v | val
                # Wir behalten nur distinkte Werte und speichern den jeweils linksmosten Startindex.
                if not next_ors or new_v != next_ors[-1][0]:
                    next_ors.append((new_v, idx))
            
            # 2. Füge das Subarray hinzu, das nur aus dem Element an Index i besteht.
            if not next_ors or val != next_ors[-1][0]:
                next_ors.append((val, i))
            
            current_ors = next_ors
            
            # 3. Zähle die "guten" Subarrays, die am aktuellen Index i enden.
            # Ein Subarray ist gut, wenn sein OR-Wert v in dem Bereich [start_idx, i] vorkommt.
            for j in range(len(current_ors)):
                v, start_idx = current_ors[j]
                # Bestimme das Ende des Bereichs für diesen spezifischen OR-Wert v.
                end_range = (current_ors[j+1][1] - 1) if j + 1 < len(current_ors) else i
                
                if v in last_pos:
                    pos = last_pos[v]
                    # Ein Subarray, das bei x beginnt und bei i endet, ist gut, wenn:
                    # a) Sein OR-Wert v entspricht (gegeben durch den Bereich [start_idx, end_range])
                    # b) Der Wert v im Subarray enthalten ist (d.h. die letzte Position von v muss >= x sein).
                    right_bound = min(end_range, pos)
                    if right_bound >= start_idx:
                        total_good += (right_bound - start_idx + 1)
                        
        return total_good

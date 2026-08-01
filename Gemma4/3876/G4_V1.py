class Solution(object):

    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """ 
        # Schritt 1: Finde das kleinste Element im Array.
        # Das kleinste Element ist entscheidend, da und nur dann ein Element 
        # verändert werden kann, wenn es einen Index j gibt, sodass nums1[i] - nums1[j] >= 1.
        # Das absolute Minimum des Arrays kann also niemals durch Subtraktion verändert werden.
        min_val = min(nums1)

        # Fall A: Das kleinste Element ist ungerade (odd).
        # Wenn das Minimum ungerade ist, können wir alle Elemente in nums2 ungerade machen:
        # - Alle bereits ungeraden Zahlen bleiben ungerade.
        # - Alle geraden Zahlen E werden zu (E - min_val), was immer ungerade ist 
        #   und aufgrund der Distinct-Constraints >= 1.
        if min_val % 2 != 0:
            return True

        # Fall B: Das kleinste Element ist gerade (even).
        # Da das Minimum gerade ist und nicht verändert werden kann, muss nums2 
        # zwingend aus nur geraden Zahlen bestehen.
        # Eine ungerade Zahl O könnte man nur durch (O - X) gerade machen, wenn X ebenfalls ungerade ist.
        # Da aber min_val gerade ist und alle anderen Zahlen in nums1 größer als min_val sind,
        # gibt es keine Garantie für ein kleineres ungerades Element. 
        # Tatsächlich: Wenn das absolute Minimum gerade ist, kann die kleinste ungerade Zahl 
        # im Array niemals gerade gemacht werden (da kein noch kleineres ungerades Element existiert).
        # Daher müssen in diesem Fall bereits ALLE Zahlen in nums1 gerade sein.
        for num in nums1:
            if num % 2 != 0:
                return False
        
        return True

"""
Dieses Modul bietet eine Lösung zur Berechnung der Summe aller sortierbaren 
ganzzahligen Teiler k eines Arrays.
"""

class Solution:
    """
    Klasse zur Analyse von Arrays hinsichtlich ihrer zyklischen Sortierbarkeit
    in Teilblöcken der Länge k.
    """

    def sortable_integers(self, nums):
        """
        Berechnet die Summe aller Teiler k von n, sodass das Array durch
        zyklische Rotationen der Teilblöcke der Länge k sortiert werden kann.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)
        
        # Finde alle Teiler von n effizient in O(sqrt(n))
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        for k in divisors:
            if self._check_k_sortable(nums, target, k):
                total_sum += k
                
        return total_sum

    def _check_k_sortable(self, nums, target, k):
        """
        Prüft, ob das Array für eine gegebene Blocklänge k sortierbar ist.
        """
        n = len(nums)
        for i in range(0, n, k):
            block_nums = nums[i : i + k]
            block_target = target[i : i + k]
            
            if not self._is_cyclic_rotation(block_nums, block_target):
                return False
        return True

    def _is_cyclic_rotation(self, block_a, block_b):
        """
        Prüft, ob block_a eine zyklische Rotation von block_b ist.
        Da block_b bereits sortiert ist, kann die Prüfung optimiert werden.
        """
        if block_a == block_b:
            return True
        
        # Suche nach der Stelle, an der das Array "springt" (nicht mehr steigend ist)
        drop_index = -1
        for i in range(len(block_a) - 1):
            if block_a[i] > block_a[i + 1]:
                if drop_index != -1:
                    # Mehr als ein Drop bedeutet: keine Rotation eines sortierten Arrays
                    return False
                drop_index = i
        
        if drop_index == -1:
            # Das Array ist bereits sortiert; falls block_a != block_b, dann False
            return block_a == block_b
        
        # Erzeuge die Rotation an der Drop-Stelle und vergleiche mit dem Zielblock
        rotated = block_a[drop_index + 1:] + block_a[:drop_index + 1]
        return rotated == block_b

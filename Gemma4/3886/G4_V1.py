class Solution(object):

    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)
        
        # Funktion zur Prüfung, ob A eine zyklische Rotation von B ist.
        # Da B bereits sortiert ist (aus dem target Array), vereinfacht sich die Prüfung.
        def is_cyclic_rotation(A, B):
            if A == B:
                return True
            
            # Suche nach der Stelle, an der das Array "springt" (nicht mehr steigend ist)
            drop_index = -1
            for i in range(len(A) - 1):
                if A[i] > A[i+1]:
                    if drop_index != -1: 
                        # Mehr als ein Drop bedeutet, es kann keine Rotation eines sortierten Arrays sein
                        return False
                    drop_index = i
            
            if drop_index == -1:
                # Das Array ist bereits sortiert; falls A != B, dann ist es keine Rotation
                return A == B
            
            # Erzeuge die Rotation und vergleiche sie mit dem Zielblock B
            rotated = A[drop_index + 1:] + A[:drop_index + 1]
            return rotated == B

        # Finde alle Teiler von n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i*i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        for k in divisors:
            possible = True
            # Prüfe jeden Block der Länge k
            for i in range(0, n, k):
                block_nums = nums[i : i + k]
                block_target = target[i : i + k]
                
                if not is_cyclic_rotation(block_nums, block_target):
                    possible = False
                    break
            
            if possible:
                total_sum += k
                
        return total_sum

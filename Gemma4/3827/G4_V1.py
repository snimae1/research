class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Wir beginnen mit 1, da die Zahl 0 (binär "0") immer als Monobit gilt 
        # und laut Constraints (0 <= n) immer im Bereich liegt.
        count = 1
        
        # Ein Monobit-Integer (außer 0) besteht aus einer Kette von Einsen.
        # Diese Zahlen folgen dem Muster: (2^k - 1) -> 1, 3, 7, 15...
        k = 1
        while True:
            monobit_value = (2**k) - 1
            if monobit_value <= n:
                count += 1
                k += 1
            else:
                break
                
        return count

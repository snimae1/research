class Solution(object):
    def countMonobit(self, n):
        count = 0
        
        for i in range(n + 1):
            binary = bin(i)[2:]  # Binärdarstellung ohne '0b'
            
            # Prüfen, ob alle Bits gleich sind
            if all(bit == binary[0] for bit in binary):
                count += 1
                
        return count

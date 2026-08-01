class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        
        freq = Counter(s)
        visited = set()
        total = 0
        
        for c in freq:
            if c in visited:
                continue
                
            # compute mirror character
            if 'a' <= c <= 'z':
                m = chr(ord('z') - (ord(c) - ord('a')))
            else:  # digit '0'..'9'
                m = chr(ord('9') - (ord(c) - ord('0')))
                
            total += abs(freq[c] - freq.get(m, 0))
            visited.add(c)
            visited.add(m)
            
        return total

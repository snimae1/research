class Solution(object):
    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        freq = Counter(s)
        ans = 0
        visited = set()

        for c in freq:
            if c in visited:
                continue

            if 'a' <= c <= 'z':
                m = chr(ord('z') - (ord(c) - ord('a')))
            else:  # digit
                m = chr(ord('9') - (ord(c) - ord('0')))

            ans += abs(freq[c] - freq.get(m, 0))
            visited.add(c)
            visited.add(m)

        return ans

class Solution(object):

    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # Wir iterieren von i = 0 bis n-1, um den kleinstmöglichen Index zu finden
        for i in range(n):
            # Überprüfung der Bedingung: s[i] muss gleich s[n - i - 1] sein
            if s[i] == s[n - i - 1]:
                return i
        
        # Wenn die Schleife komplett durchläuft, ohne ein Match zu finden,
        # geben wir -1 zurück.
        return -1

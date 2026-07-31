class Solution(object):
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0 # Laut Constraints ist n >= 2, aber zur Sicherheit.

        # Schritt 1: DP-Tabelle für Palindrome erstellen O(N^2)
        # isPal[i][j] ist True, wenn s[i...j] ein Palindrom ist
        isPal = [[False] * n for _ in range(n)]
        
        # Alle Einzelzeichen sind Palindrome
        for i in range(n):
            isPal[i][i] = True
            
        # Alle Doppelzeichen prüfen
        for i in range(n - 1):
            if s[i] == s[i+1]:
                isPal[i][i+1] = True
                
        # Längere Teilstrings prüfen (Bottom-up DP)
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and isPal[i+1][j-1]:
                    isPal[i][j] = True

        max_len = 0
        
        # Schritt 2: Über alle möglichen Zentren expandieren O(N^2)
        # Wir prüfen jedes mögliche Zentrum eines Palindroms.
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)
            
            # Expandiere so lange, wie es ein perfektes Palindrom ist
            while left >= 0 and right < n and s[left] == s[right]:
                # Ein Teilstring, der bereits ein Palindrom ist und Länge >= 2 hat,
                # ist immer auch "almost-palindromic" (entferne das mittlere Element).
                current_len = right - left + 1
                if current_len >= 2:
                    max_len = max(max_len, current_len)
                left -= 1
                right += 1
            
            # Wenn wir hier sind, ist s[left] != s[right].
            # Dieser Teilstring [left, right] könnte fast palindromisch sein,
            # wenn man entweder s[left] oder s[right] entfernt.
            if left >= 0 and right < n:
                # Prüfen, ob das Entfernen von einem Zeichen ein Palindrom ergibt
                # Fall A: Entferne s[left] -> prüfen ob s[left+1...right] ein Palindrom ist
                # Fall B: Entferne s[right] -> prüfen ob s[left...right-1] ein Palindrom ist
                if isPal[left + 1][right] or isPal[left][right - 1]:
                    max_len = max(max_len, right - left + 1)
        
        # Sonderfall: Wenn kein langes fast-palindromisches Substring gefunden wurde,
        # ist jede Kombination aus zwei Zeichen (länge 2) fast palindromisch,
        # da das Entfernen eines Zeichens immer ein Palindrom der Länge 1 ergibt.
        return max(max_len, 2 if n >= 2 else 0)

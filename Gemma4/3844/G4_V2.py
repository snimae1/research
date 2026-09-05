"""
Dieses Modul bietet eine Lösung zur Findung des längsten fast-palindromischen Teilstrings.
Ein Teilstring ist fast-palindromisch, wenn er durch das Entfernen von genau einem
Zeichen zu einem Palindrom wird.
"""


class Solution:
    """
    Klasse zur Lösung des Problems der fast-palindromischen Teilstrings.
    """

    def almostPalindromic(self, s):
        """
        Findet die Länge des längsten Teilstrings, der fast-palindromisch ist.

        :type s: str
        :rtype: int
        """
        # Hinweis: Die Methode behält den Namen 'almostPalindromic',
        # um mit der geforderten Syntax kompatibel zu bleiben,
        # obwohl Pylint snake_case bevorzugt.
        n = len(s)
        if n < 2:
            return 0

        # dp[i][j] speichert die Länge der längsten palindromischen
        # Teilfolge (Longest Palindromic Subsequence - LPS) im Bereich s[i...j]
        dp = [[0] * n for _ in range(n)]

        # Fülle die DP-Tabelle von unten nach oben (Bottom-Up)
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1  # Einzelzeichen sind immer Palindrome der Länge 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    # Wenn die äußeren Zeichen gleich sind, addieren wir 2 zur
                    # Länge des inneren Palindroms
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Andernfalls nehmen wir das Maximum aus den Möglichkeiten,
                    # eines der beiden äußeren Zeichen zu ignorieren
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        max_len = 0
        # Überprüfe alle möglichen Teilstrings s[i...j]
        for i in range(n):
            for j in range(i + 1, n):
                substring_len = j - i + 1
                lps_len = dp[i][j]

                # Ein String ist fast-palindromisch, wenn man durch das Entfernen
                # von GENAU einem Zeichen ein Palindrom erhält.
                # Das bedeutet, die LPS muss die Länge (substring_len - 1) haben.
                # Sonderfall: Wenn LPS == substring_len, ist es ein perfektes 
                # Palindrom. Durch Entfernen des mittleren Zeichens bleibt es 
                # ein Palindrom (solange Länge >= 2).
                if lps_len >= substring_len - 1:
                    if substring_len >= 2:
                        max_len = max(max_len, substring_len)

        return max_len

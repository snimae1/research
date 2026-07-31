class Solution(object):
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n

        # pal[i][j] == 1  ->  s[i:j+1] ist ein Palindrom
        # almost[i][j] == 1 ->  s[i:j+1] ist fast‑palindromisch
        pal = [bytearray(n) for _ in range(n)]
        almost = [bytearray(n) for _ in range(n)]

        max_len = 1

        # Länge 1
        for i in range(n):
            pal[i][i] = 1
            almost[i][i] = 1

        # DP über alle Längen
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Palindrom-Eigenschaft
                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = 1
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

                # fast‑palindromisch
                if pal[i][j]:
                    almost[i][j] = 1
                else:
                    if s[i] == s[j]:
                        # innen muss fast‑palindromisch sein
                        if length > 2 and almost[i + 1][j - 1]:
                            almost[i][j] = 1
                    else:
                        # ungleiche Ränder: einer der Ränder muss entfernt werden
                        if pal[i + 1][j] or pal[i][j - 1]:
                            almost[i][j] = 1

                if almost[i][j]:
                    max_len = max(max_len, length)

        return max_len

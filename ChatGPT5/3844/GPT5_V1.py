class Solution(object):
    def almostPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Prüft, ob s[l:r+1] ein Palindrom ist.
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 2

        # Alle möglichen Teilstrings testen
        # (O(n²), da is_pal insgesamt amortisiert O(n) kostet,
        # aber höchstens einmal pro Teilstring nach dem ersten Fehler aufgerufen wird.)
        for l in range(n):
            for r in range(l + 1, n):
                i, j = l, r

                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1

                if i >= j:
                    # Bereits Palindrom.
                    ans = max(ans, r - l + 1)
                else:
                    # Genau ein Zeichen löschen.
                    if is_pal(i + 1, j) or is_pal(i, j - 1):
                        ans = max(ans, r - l + 1)

        return ans

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        t = "".join(sorted(s))

        if s == t:
            return 0

        # Das erste Zeichen kann niemals verändert werden, da das gesamte
        # Stringsegment nicht sortiert werden darf.
        if s[0] != t[0]:
            return -1

        ans = 0
        i = 1
        while i < n:
            if s[i] > s[i - 1]:
                i += 1
                continue

            ans += 1
            while i < n and s[i] <= s[i - 1]:
                i += 1

        return ans

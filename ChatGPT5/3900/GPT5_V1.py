class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        total0 = s.count('0')
        total1 = n - total0

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if s[i] == '1' else -1)

        first = {}
        ans = 0

        for i in range(n + 1):
            if pref[i] not in first:
                first[pref[i]] = i

            j = first[pref[i]]
            length = i - j

            if length <= ans:
                continue

            ones = (length + pref[i] - pref[j]) // 2
            zeros = length - ones

            out0 = total0 - zeros
            out1 = total1 - ones

            need0 = need1 = 0

            if zeros > ones:
                d = (zeros - ones) // 2
                need1 = d
                need0 = d
            elif ones > zeros:
                d = (ones - zeros) // 2
                need0 = d
                need1 = d

            if out0 >= need0 and out1 >= need1:
                ans = length

        return ans

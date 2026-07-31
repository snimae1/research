class Solution(object):
    def isDigitorialPermutation(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        digits = str(n)

        total = 0
        for ch in digits:
            total += fact[ord(ch) - ord('0')]

        return sorted(digits) == sorted(str(total))

class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        s = str(n)
        d = str(x)
        # Check that the number does not start with digit x
        if s[0] == d:
            return False
        # Check that the number contains at least one occurrence of x
        return d in s

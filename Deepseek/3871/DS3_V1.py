class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_commas = 0
        k = 1
        while True:
            start = 10 ** (3 * k)          # smallest number with k commas
            if start > n:
                break
            end = 10 ** (3 * k + 3) - 1    # largest number with k commas
            count = min(n, end) - start + 1
            total_commas += count * k
            k += 1
        return total_commas

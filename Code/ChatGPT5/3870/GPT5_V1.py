class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0

        # Zahlen mit mindestens einer Komma: 1.000+
        if n >= 1000:
            total += n - 999

        # Zahlen mit mindestens zwei Kommas: 1.000.000+
        if n >= 1000000:
            total += n - 999999

        # Zahlen mit mindestens drei Kommas: 1.000.000.000+
        if n >= 1000000000:
            total += n - 999999999

        # Zahlen mit mindestens vier Kommas: 1.000.000.000.000+
        if n >= 1000000000000:
            total += n - 999999999999

        return total

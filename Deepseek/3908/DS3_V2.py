"""Module for validating a number based on digit conditions."""

class Solution(object):
    """Solution class providing number validation."""

    def validDigit(self, n, x):
        """
        Check if number n is valid according to digit x.

        A number is valid if it contains at least one occurrence of digit x,
        and it does not start with digit x.

        :type n: int
        :type x: int
        :rtype: bool
        """
        number_str = str(n)
        digit_str = str(x)
        # Check that the number does not start with digit x
        if number_str[0] == digit_str:
            return False
        # Check that the number contains at least one occurrence of x
        return digit_str in number_str

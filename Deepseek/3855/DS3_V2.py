"""
Solution for summing all numbers formed by k digits from range [l, r].
"""

class Solution(object):
    """
    Provides a method to compute the sum of all possible k-digit numbers
    where each digit is independently chosen from the inclusive range [l, r].
    Leading zeros are allowed if 0 is in the range.
    """
    # pylint: disable=useless-object-inheritance
    # pylint: disable=invalid-name
    def sumOfNumbers(self, l, r, k):
        """
        Computes the sum modulo 10^9 + 7.

        The formula used:
            Let n = number of possible digits, S = sum of possible digits.
            For each position i (0 = units, 1 = tens, ...) there are n^(k-1)
            choices for the other positions, and the digit at position i
            contributes S * n^(k-1) * 10^i.
            Summing over all k positions gives:
                S * n^(k-1) * (10^k - 1) / 9   (mod 10^9 + 7)

        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        mod = 1000000007

        # Number of valid digits and their sum
        digit_count = r - l + 1
        digit_sum = (l + r) * digit_count // 2

        # If there are no digits (should not happen per constraints), return 0
        if digit_count == 0:
            return 0

        # Calculate n^(k-1) modulo mod
        pow_digit_count = pow(digit_count, k - 1, mod)

        # Calculate geometric series (10^k - 1) / 9 modulo mod
        pow_10 = pow(10, k, mod)
        inverse_9 = pow(9, mod - 2, mod)   # modular inverse of 9 mod (10^9+7)
        geometric_sum = (pow_10 - 1) * inverse_9 % mod

        # Combine all parts
        result = (digit_sum * pow_digit_count) % mod
        result = (result * geometric_sum) % mod

        return result

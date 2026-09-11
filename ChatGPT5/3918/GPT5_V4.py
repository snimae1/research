"""Calculate the sum of primes between a number and its reversed value."""

# pylint: disable=invalid-name


class Solution(object):
    """Provide a solution for calculating the sum of primes in a range."""

    # pylint: disable=too-few-public-methods

    def sumOfPrimesInRange(self, n):
        """
        Calculate the sum of all primes between n and its reversed value.

        :param n: The input integer.
        :type n: int
        :return: The sum of all prime numbers in the range.
        :rtype: int
        """
        # Reverse the digits of n.
        reversed_number = int(str(n)[::-1])

        # Determine the lower and upper bounds of the range.
        lower_bound = min(n, reversed_number)
        upper_bound = max(n, reversed_number)

        def is_prime(number):
            """Return True if number is prime, otherwise False."""
            if number < 2:
                return False

            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    return False
                divisor += 1

            return True

        # Add every prime number in the specified range.
        prime_sum = 0
        for number in range(lower_bound, upper_bound + 1):
            if is_prime(number):
                prime_sum += number

        return prime_sum

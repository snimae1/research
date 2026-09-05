"""
Module for counting commas in numbers from 1 to n.
"""


class Solution:
    """
    Provides a method to count total commas used in standard formatting
    for all integers from 1 to n.
    """

    # pylint: disable=invalid-name
    def countCommas(self, n):
        """
        Compute the total number of commas used when writing all integers
        from 1 to n (inclusive) in standard number formatting.

        A comma is inserted after every three digits from the right.
        Numbers with fewer than 4 digits contain no commas.

        :type n: int
        :rtype: int
        """
        total_commas = 0
        group = 1  # number of commas in numbers of this magnitude

        while True:
            # Smallest number that has 'group' commas
            start = 10 ** (3 * group)
            if start > n:
                break

            # Largest number that has 'group' commas
            end = 10 ** (3 * group + 3) - 1

            # How many numbers in [start, min(n, end)] have this many commas
            count = min(n, end) - start + 1
            total_commas += count * group

            group += 1

        return total_commas

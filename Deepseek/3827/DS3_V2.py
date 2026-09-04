"""
Solution for counting Monobit integers up to n.
"""


class Solution:
    """Provides methods to solve the Monobit counting problem."""

    # Pylint-Kommentare deaktivieren stilistische Warnungen,
    # da die Methodensignatur von der Aufgabenstellung vorgegeben ist.
    # pylint: disable=too-few-public-methods
    # pylint: disable=invalid-name
    def countMonobit(self, n: int) -> int:
        """
        Return the count of integers in [0, n] whose binary representation
        consists of identical bits.

        A Monobit number is either 0 or a number of the form 2^k - 1
        (i.e., all bits set to 1). The largest such number <= n is
        2^k - 1 with k = floor(log2(n + 1)). Therefore, the total count
        is k + 1, which equals the bit length of n + 1.
        """
        return (n + 1).bit_length()

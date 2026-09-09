"""Solution for counting Monobit integers."""


class Solution:
    """Provide a method for counting Monobit integers."""

    # pylint: disable=too-few-public-methods

    def countMonobit(self, n):
        """Return the number of Monobit integers in the range [0, n]."""
        # pylint: disable=invalid-name

        count = 1  # 0 ist immer eine Monobit-Zahl.
        value = 1

        # Positive Monobit-Zahlen haben die Form 1, 3, 7, 15, ...
        while value <= n:
            count += 1
            value = (value << 1) | 1

        return count

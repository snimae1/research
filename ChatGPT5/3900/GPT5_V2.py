```python
"""Solution for finding the longest balanced substring after at most one swap."""


class Solution(object):
    """Find the maximum possible length of a balanced substring."""

    def _can_fix_imbalance(self, left, right, balance, first_zero,
                           last_zero, first_one, last_one):
        """Return whether one swap can balance the substring."""

        if balance == 2:
            # We need a zero outside the substring.
            return first_zero < left or last_zero >= right

        if balance == -2:
            # We need a one outside the substring.
            return first_one < left or last_one >= right

        return False

    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Prefix balance:
        # +1 for '1' and -1 for '0'.
        # Equal prefix balances define a balanced substring.
        balance = 0
        first_position = {0: 0}

        first_zero = s.find('0')
        first_one = s.find('1')
        last_zero = s.rfind('0')
        last_one = s.rfind('1')

        best = 0

        for right, char in enumerate(s, 1):
            balance += 1 if char == '1' else -1

            # A substring with balance 0 is already balanced.
            if balance in first_position:
                left = first_position[balance]
                best = max(best, right - left)
            else:
                first_position[balance] = right

            # A substring with balance +2 or -2 can become balanced
            # by swapping one character inside with the opposite
            # character outside the substring.
            for target_balance in (balance - 2, balance + 2):
                if target_balance not in first_position:
                    continue

                left = first_position[target_balance]
                length = right - left

                if length <= best:
                    continue

                difference = balance - target_balance

                if self._can_fix_imbalance(
                        left, right, difference,
                        first_zero, last_zero,
                        first_one, last_one):
                    best = length

        return best
```

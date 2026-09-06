"""
Solution for finding the longest balanced substring after at most one swap.
"""
class Solution:
    """Provides method to compute the longest balanced substring."""

    # pylint: disable=invalid-name
    def longestBalanced(self, s):
        """
        Returns the maximum length of a balanced substring that can be selected
        after performing at most one swap between any two characters in s.

        :type s: str
        :rtype: int
        """
        n = len(s)
        total0 = s.count('0')
        total1 = n - total0

        max_without_swap = self._max_len_without_swap(s)
        max_swap_0_to_1 = self._max_len_with_swap(s, total0, total1, '0')
        max_swap_1_to_0 = self._max_len_with_swap(s, total0, total1, '1')

        return max(max_without_swap, max_swap_0_to_1, max_swap_1_to_0)

    def _max_len_without_swap(self, s):
        """Finds the longest substring with equal number of '0' and '1'."""
        max_len = 0
        first_occurrence = {0: 0}
        prefix_sum = 0
        for index, char in enumerate(s, 1):
            prefix_sum += 1 if char == '1' else -1
            if prefix_sum in first_occurrence:
                max_len = max(max_len, index - first_occurrence[prefix_sum])
            else:
                first_occurrence[prefix_sum] = index
        return max_len

    def _max_len_with_swap(self, s, total0, total1, swap_char):
        """
        Computes the longest substring that can be balanced by swapping
        one occurrence of swap_char with the opposite character.

        swap_char: '0' to swap a zero into a one (prefix sum +2)
                   '1' to swap a one into a zero (prefix sum -2)
        """
        total_swap = total0 if swap_char == '0' else total1
        # Change in prefix sum (#1 - #0) caused by the swap
        delta = 2 if swap_char == '0' else -2

        max_len = 0
        first_all = {0: 0}          # earliest index for each prefix sum
        first_with_swap_left = {}   # earliest index where count of swap_char > 0
        prefix_sum = 0
        count_swap = 0              # number of swap_char in the current prefix

        for index, char in enumerate(s, 1):
            if char == '1':
                prefix_sum += 1
                if swap_char == '1':
                    count_swap += 1
            else:
                prefix_sum -= 1
                if swap_char == '0':
                    count_swap += 1

            target = prefix_sum - delta

            # Case A: there is at least one swap_char to the left of the substring
            if target in first_with_swap_left:
                max_len = max(max_len, index - first_with_swap_left[target])

            # Case B: there is at least one swap_char to the right of the substring
            if count_swap < total_swap and target in first_all:
                max_len = max(max_len, index - first_all[target])

            # Update structures for future start positions
            if prefix_sum not in first_all:
                first_all[prefix_sum] = index
            if count_swap > 0 and prefix_sum not in first_with_swap_left:
                first_with_swap_left[prefix_sum] = index

        return max_len

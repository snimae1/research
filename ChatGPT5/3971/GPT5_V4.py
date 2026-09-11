"""Efficient solution for maximizing the total value of repeated selections."""

# pylint: disable=too-few-public-methods


class Solution:
    """Solve the maximum total value selection problem."""

    # The method name is required by the problem specification.
    # pylint: disable=invalid-name
    def maxTotalValue(self, value, decay, m):
        """
        Return the maximum total value obtainable with at most m selections.

        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        modulo = 10**9 + 7

        def count_and_sum(threshold):
            """
            Count and sum all values greater than or equal to threshold.
            """
            selection_count = 0
            total_value = 0

            for initial_value, decrease in zip(value, decay):
                if initial_value < threshold:
                    continue

                # Number of terms satisfying:
                # initial_value - decrease * (k - 1) >= threshold
                term_count = (
                    (initial_value - threshold) // decrease + 1
                )

                selection_count += term_count

                # Sum of the arithmetic sequence.
                last_value = (
                    initial_value - decrease * (term_count - 1)
                )

                total_value += (
                    term_count * (initial_value + last_value) // 2
                )

            return selection_count, total_value

        # If fewer than m positive selections exist, take all of them.
        positive_count, positive_sum = count_and_sum(1)

        if positive_count <= m:
            return positive_sum % modulo

        # Binary search for the largest threshold such that
        # at least m values are greater than or equal to it.
        lower_bound = 1
        upper_bound = max(value)

        while lower_bound < upper_bound:
            middle = (lower_bound + upper_bound + 1) // 2
            selection_count, _ = count_and_sum(middle)

            if selection_count >= m:
                lower_bound = middle
            else:
                upper_bound = middle - 1

        threshold = lower_bound
        selection_count, total_value = count_and_sum(threshold)

        # Remove excess values equal to the threshold.
        excess_selections = selection_count - m
        total_value -= excess_selections * threshold

        return total_value % modulo

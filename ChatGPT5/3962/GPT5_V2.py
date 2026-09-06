```python
"""Solution for maximizing a subarray sum using at most k swaps."""

from bisect import insort


# pylint: disable=too-few-public-methods
class Solution:
    """Solve the maximum subarray sum problem with limited swaps."""

    # pylint: disable=invalid-name
    def maxSum(self, nums, k):
        """
        Return the maximum possible subarray sum after at most k swaps.

        For every possible subarray, the algorithm determines which small
        elements inside the subarray should be exchanged with large positive
        elements outside the subarray.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        array_length = len(nums)
        best_sum = max(nums)

        for left in range(array_length):
            best_sum = max(
                best_sum,
                self._evaluate_subarrays_from_left(nums, k, left)
            )

        return best_sum

    @staticmethod
    def _evaluate_subarrays_from_left(nums, k, left):
        """
        Evaluate all subarrays starting at the given left index.

        The inside values are maintained in sorted order. For every right
        boundary, the best possible improvement using at most k swaps is
        calculated.
        """
        array_length = len(nums)
        inside_values = []
        current_sum = 0
        best_sum = float("-inf")

        for right in range(left, array_length):
            current_sum += nums[right]
            insort(inside_values, nums[right])

            outside_values = Solution._get_positive_outside_values(
                nums,
                left,
                right
            )

            candidate_sum = Solution._calculate_best_sum(
                current_sum,
                inside_values,
                outside_values,
                k
            )

            best_sum = max(best_sum, candidate_sum)

        return best_sum

    @staticmethod
    def _get_positive_outside_values(nums, left, right):
        """
        Return all positive values outside the current subarray.

        Only positive values can improve the subarray sum when swapped in.
        """
        outside_values = [
            nums[index]
            for index in range(len(nums))
            if (index < left or index > right) and nums[index] > 0
        ]

        outside_values.sort(reverse=True)
        return outside_values

    @staticmethod
    def _calculate_best_sum(
            current_sum,
            inside_values,
            outside_values,
            max_swaps):
        """
        Calculate the best sum obtainable with at most max_swaps swaps.
        """
        best_sum = current_sum
        removed_sum = 0
        added_sum = 0

        swap_count = min(
            max_swaps,
            len(inside_values),
            len(outside_values)
        )

        for index in range(swap_count):
            removed_sum += inside_values[index]
            added_sum += outside_values[index]

            improved_sum = current_sum - removed_sum + added_sum
            best_sum = max(best_sum, improved_sum)

        return best_sum
```

"""Efficient solution for counting subarrays with bounded cost."""

from collections import deque

class Solution(object):  # pylint: disable=too-few-public-methods
"""Provide a solution for counting subarrays with cost at most k."""

```
def countSubarrays(self, nums, k):  # pylint: disable=invalid-name
    """
    Count subarrays whose cost is less than or equal to k.

    The cost of a subarray is defined as:

        (maximum value - minimum value) * subarray length

    Two monotonic deques are used to efficiently track the maximum
    and minimum values in the current sliding window.

    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Store indices in decreasing value order.
    max_deque = deque()

    # Store indices in increasing value order.
    min_deque = deque()

    left = 0
    valid_subarrays = 0

    for right, value in enumerate(nums):
        # Remove smaller values because they can no longer become
        # the maximum while 'value' remains in the window.
        while max_deque and nums[max_deque[-1]] <= value:
            max_deque.pop()
        max_deque.append(right)

        # Remove larger values because they can no longer become
        # the minimum while 'value' remains in the window.
        while min_deque and nums[min_deque[-1]] >= value:
            min_deque.pop()
        min_deque.append(right)

        # Shrink the window until its cost satisfies the condition.
        while (
            (nums[max_deque[0]] - nums[min_deque[0]])
            * (right - left + 1)
            > k
        ):
            if max_deque[0] == left:
                max_deque.popleft()

            if min_deque[0] == left:
                min_deque.popleft()

            left += 1

        # Every subarray ending at 'right' and starting between
        # 'left' and 'right' is valid.
        valid_subarrays += right - left + 1

    return valid_subarrays
```

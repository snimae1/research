```python
"""Solution for repeatedly merging equal adjacent elements."""


# The class and method names are required by the coding platform.
# pylint: disable=invalid-name,too-few-public-methods
class Solution:
    """Provide the solution for merging adjacent equal numbers."""

    def mergeAdjacent(self, nums):
        """
        Merge equal adjacent elements until no further merge is possible.

        The leftmost possible merge is handled implicitly by processing the
        input from left to right with a stack.

        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for number in nums:
            result.append(number)

            # A merge can create another equal adjacent pair, so continue
            # merging until the end of the list contains no equal pair.
            while len(result) >= 2 and result[-1] == result[-2]:
                value = result.pop()
                result.pop()
                result.append(value * 2)

        return result
```

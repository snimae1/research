```python
"""Solution for finding the maximum number of fixed points."""

# pylint: disable=invalid-name,too-few-public-methods


class Solution(object):
    """Compute the maximum number of fixed points after deletions."""

    def maxFixedPoints(self, nums):
        """
        Find the maximum number of fixed points.

        :type nums: List[int]
        :rtype: int
        """
        candidates = []

        # A value x can become a fixed point only if x <= its
        # original index.  The value x determines its new index.
        for index, value in enumerate(nums):
            if value <= index:
                distance = index - value
                candidates.append((value, distance))

        if not candidates:
            return 0

        # Coordinate compression for the second dimension.
        distances = sorted(set(distance for _, distance in candidates))
        position = {
            distance: index + 1
            for index, distance in enumerate(distances)
        }

        # Group candidates by their target index (their value).
        candidates.sort()

        tree = [0] * (len(distances) + 1)

        def query(index):
            """Return the best result for distances <= index."""
            result = 0

            while index > 0:
                result = max(result, tree[index])
                index -= index & -index

            return result

        def update(index, value):
            """Update the Fenwick Tree with a better result."""
            while index < len(tree):
                tree[index] = max(tree[index], value)
                index += index & -index

        answer = 0
        start = 0

        # Values must be strictly increasing.  Therefore candidates
        # with the same value are queried first and updated afterwards.
        while start < len(candidates):
            end = start

            while (
                end < len(candidates)
                and candidates[end][0] == candidates[start][0]
            ):
                end += 1

            updates = []

            for _, distance in candidates[start:end]:
                index = position[distance]
                best = query(index) + 1
                updates.append((index, best))
                answer = max(answer, best)

            for index, best in updates:
                update(index, best)

            start = end

        return answer
```

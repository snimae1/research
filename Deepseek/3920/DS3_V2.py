"""
Solution for the "Maximum Fixed Points" problem.
"""
class Solution:
    def maxFixedPoints(self, nums):
        """
        Given an array nums, return the maximum number of fixed points
        achievable after deleting any number of elements.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # groups[value] stores all differences (i - value) for elements that
        # could become fixed points if we delete (i - value) elements before them.
        groups = [[] for _ in range(n)]
        for i, val in enumerate(nums):
            if val <= i:
                # Only if val <= i, it's possible to delete enough elements
                # from the left to make nums[i] == i after shifting.
                groups[val].append(i - val)

        # Fenwick tree (Binary Indexed Tree) for prefix maximum queries.
        # We need to find the maximum length of a chain of selected elements
        # with strictly increasing values and non-decreasing differences.
        bit_size = n + 2
        bit = [0] * bit_size

        def bit_update(index, value):
            """Update BIT at index with given value (take max)."""
            while index < bit_size:
                if value > bit[index]:
                    bit[index] = value
                index += index & -index

        def bit_query(index):
            """Query prefix maximum up to index."""
            result = 0
            while index > 0:
                if bit[index] > result:
                    result = bit[index]
                index -= index & -index
            return result

        answer = 0
        # Process values in increasing order (since selected values must be strictly increasing)
        for value in range(n):
            if not groups[value]:
                continue
            # Compute DP for all differences of this value using current BIT state
            # (which contains only results from smaller values).
            updates = []
            for diff in groups[value]:
                # diff is in range [0, n-1]; BIT is 1-indexed, so query diff+1
                best_prev = bit_query(diff + 1)
                updates.append((diff, best_prev + 1))
            # Update BIT with new DP values from this value group
            for diff, new_val in updates:
                bit_update(diff + 1, new_val)
                answer = max(answer, new_val)

        return answer

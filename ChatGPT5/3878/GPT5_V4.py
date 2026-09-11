"""Count good subarrays based on their bitwise OR."""


class Solution:
    """Solution for counting good subarrays."""

    @staticmethod
    def _add_or_group(groups, value, start):
        """Add an OR value to the current groups."""
        if value in groups:
            groups[value][0] = min(groups[value][0], start)
            groups[value][1] = max(groups[value][1], start)
        else:
            groups[value] = [start, start]

    def countGoodSubarrays(self, nums):  # pylint: disable=invalid-name
        """
        Count subarrays whose OR is contained as an element.

        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        previous = {}
        last_position = {}

        for end, value in enumerate(nums):
            current = {}

            # Subarray containing only nums[end].
            self._add_or_group(current, value, end)

            # Extend every OR group ending at the previous position.
            for or_value, (left, _) in previous.items():
                new_or = or_value | value
                self._add_or_group(current, new_or, left)

            last_position[value] = end

            # Check whether the OR value occurs inside the subarray.
            for or_value, (left, right) in current.items():
                position = last_position.get(or_value)

                if position is not None and position >= left:
                    answer += min(right, position) - left + 1

            previous = current

        return answer

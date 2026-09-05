"""Determine which block sizes can sort an integer array by cyclic rotations."""


class Solution:
    """Solve the sortable-integers problem."""

    @staticmethod
    def _is_rotation(source, target):
        """Return True if target is a cyclic rotation of source."""
        if len(source) != len(target):
            return False

        # A rotation of source occurs as a contiguous part of source + source.
        doubled = source + source
        size = len(source)

        for start in range(size):
            if doubled[start:start + size] == target:
                return True

        return False

    @staticmethod
    def _is_sortable_for_k(nums, sorted_nums, k):
        """Check whether blocks of size k can be rotated into sorted order."""
        for start in range(0, len(nums), k):
            original_block = nums[start:start + k]
            sorted_block = sorted_nums[start:start + k]

            if not Solution._is_rotation(original_block, sorted_block):
                return False

        return True

    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        answer = 0

        # Only divisors of n can be used as block sizes.
        divisors = self._get_divisors(n)

        for k in divisors:
            if self._is_sortable_for_k(nums, sorted_nums, k):
                answer += k

        return answer

    @staticmethod
    def _get_divisors(number):
        """Return all positive divisors of number."""
        divisors = []
        divisor = 1

        while divisor * divisor <= number:
            if number % divisor == 0:
                divisors.append(divisor)

                other = number // divisor
                if divisor != other:
                    divisors.append(other)

            divisor += 1

        return divisors

"""Determine whether an array can be made uniform in parity."""


class Solution(object):
    """Solve the uniform array problem."""

    def uniformArray(self, nums1):
        """
        Check whether all elements can be made odd or all even.

        :param nums1: List of distinct integers.
        :return: True if a uniform parity is possible, otherwise False.
        """
        smallest_odd = None

        # Find the smallest odd number in the input.
        for number in nums1:
            if number % 2 == 1:
                if smallest_odd is None or number < smallest_odd:
                    smallest_odd = number

        # Check whether every element can have the requested parity.
        def can_make_parity(target_parity):
            for number in nums1:
                if number % 2 != target_parity:
                    # Changing parity requires subtracting a smaller odd number.
                    if smallest_odd is None or smallest_odd >= number:
                        return False
            return True

        # It is sufficient if either all numbers can become even
        # or all numbers can become odd.
        return can_make_parity(0) or can_make_parity(1)

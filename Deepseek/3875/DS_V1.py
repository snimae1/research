class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Count how many odd numbers are in nums1
        odd_count = sum(1 for x in nums1 if x % 2 == 1)
        
        # We can always construct the required array:
        # - If odd_count != 1, we can make all numbers even.
        # - If odd_count >= 1, we can make all numbers odd.
        # Since odd_count is either 0, 1, or >=2, at least one condition always holds.
        return True

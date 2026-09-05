"""
This module provides a solution to find the maximum length of an arithmetic 
subarray that can be achieved by replacing at most one element in a given array.
"""

class Solution:
    """
    A class containing the logic to calculate the longest arithmetic subarray
    after potentially replacing one element.
    """

    def longest_arithmetic(self, nums):
        """
        Calculates the maximum length of an arithmetic subarray 
        after replacing at most one element.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        # fwd[i]: Length of the arithmetic sequence ending at index i
        fwd = [0] * n
        fwd[0], fwd[1] = 1, 2
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                fwd[i] = fwd[i-1] + 1
            else:
                fwd[i] = 2

        # bwd[i]: Length of the arithmetic sequence starting at index i
        bwd = [0] * n
        bwd[n-1], bwd[n-2] = 1, 2
        for i in range(n-3, -1, -1):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                bwd[i] = bwd[i+1] + 1
            else:
                bwd[i] = 2

        # Initial answer: Extend any existing sequence by one element
        ans = 0
        for i in range(n):
            if i > 0:
                ans = max(ans, fwd[i-1] + 1)
            if i < n - 1:
                ans = max(ans, bwd[i+1] + 1)

        # Check every index k as a potential bridge point
        for k in range(1, n - 1):
            ans = max(ans, self._get_bridge_length(nums, fwd, bwd, k))

        return min(ans, n)

    def _get_bridge_length(self, nums, fwd, bwd, k):
        """
        Helper method to calculate the length of a sequence formed by 
        replacing the element at index k.
        """
        n = len(nums)
        diff_sum = nums[k+1] - nums[k-1]
        
        if diff_sum % 2 != 0:
            return 0
            
        d = diff_sum // 2
        
        # Determine length contributed by the left side
        left_len = fwd[k-1] if (k - 2 >= 0 and nums[k-1] - nums[k-2] == d) else 2
        
        # Determine length contributed by the right side
        right_len = bwd[k+1] if (k + 2 < n and nums[k+2] - nums[k+1] == d) else 2
        
        # The bridge consists of: left_len elements + the replaced element at k
        # But left_len already includes the element at k-1, and right_len includes k+1.
        # To avoid overcounting the base elements (k-1 and k+1), 
        # we calculate it as: (left_len) + 1 (for k) + (right_len - 1) 
        # Wait, the logic is simpler:
        # if nums[k-1] is the end of a seq of length L1 with diff d, 
        # and nums[k+1] is the start of a seq of length L2 with diff d,
        # the total length is L1 + 1 + L2.
        
        # Correcting the logic for clarity:
        l_val = fwd[k-1] if (k - 2 >= 0 and nums[k-1] - nums[k-2] == d) else 1
        r_val = bwd[k+1] if (k + 2 < n and nums[k+2] - nums[k+1] == d) else 1
        
        return l_val + 1 + r_val

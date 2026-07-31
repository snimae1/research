class Solution(object):

    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        CAP = total_sum + 1  # product > total_sum can never equal any left sum
        
        # right_prod[i] = product of nums[i...n-1] capped at CAP
        right_prod = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            prod = nums[i] * right_prod[i + 1]
            if prod > CAP:
                right_prod[i] = CAP
            else:
                right_prod[i] = prod
        
        left_sum = 0
        for i in range(n):
            # product strictly right of index i is right_prod[i + 1]
            if left_sum == right_prod[i + 1]:
                return i
            left_sum += nums[i]
        
        return -1

import math

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Build prefixGcd array
        prefixGcd = []
        current_max = nums[0]
        for num in nums:
            if num > current_max:
                current_max = num
            g = math.gcd(num, current_max)
            prefixGcd.append(g)

        # Step 2: Sort the array
        prefixGcd.sort()

        # Step 3: Pair up and sum gcd of pairs
        total = 0
        n = len(prefixGcd)
        # Only form n // 2 pairs, ignore the middle element if n is odd
        for i in range(n // 2):
            total += math.gcd(prefixGcd[i], prefixGcd[n - 1 - i])

        return total

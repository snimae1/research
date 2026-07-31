from math import gcd

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd = []
        mx = 0

        # Construct prefixGcd
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(gcd(x, mx))

        # Sort
        prefixGcd.sort()

        # Pair smallest with largest
        ans = 0
        i, j = 0, len(prefixGcd) - 1
        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans

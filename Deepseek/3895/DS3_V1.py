class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        total = 0
        target = str(digit)
        for num in nums:
            total += str(num).count(target)
        return total

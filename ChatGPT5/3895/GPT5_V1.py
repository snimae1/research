class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        target = str(digit)
        count = 0

        for num in nums:
            for ch in str(num):
                if ch == target:
                    count += 1

        return count

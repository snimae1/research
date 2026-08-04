class Solution(object):
    def minimumPrefixLength(self, nums):
        n = len(nums)
        
        # Start von hinten und finde das längste strikt steigende Suffix
        i = n - 1
        while i > 0 and nums[i - 1] < nums[i]:
            i -= 1
        
        # i ist die minimale Prefix-Länge, die entfernt werden muss
        return i

class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for x in nums:
            # While the new value equals the top of the stack, merge them.
            # The sum becomes the new value, and we continue checking upwards.
            while stack and stack[-1] == x:
                x += stack.pop()
            stack.append(x)
        return stack

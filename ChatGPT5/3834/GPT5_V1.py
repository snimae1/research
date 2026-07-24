class Solution(object):
    def mergeAdjacent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []

        for x in nums:
            stack.append(x)

            while len(stack) >= 2 and stack[-1] == stack[-2]:
                val = stack.pop()
                stack.pop()
                stack.append(val * 2)

        return stack

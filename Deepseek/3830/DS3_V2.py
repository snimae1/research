"""
Module providing solution for longest alternating subarray problem.
"""
# pylint: disable=invalid-name, too-few-public-methods, too-many-branches

class Solution:
    """
    Provides method to compute the maximum length of an alternating subarray
    after optionally removing one element.
    """
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1

        # left_up[i] : längste alternierende Sequenz, die bei i endet
        #               und deren letzter Vergleich '>' ist (nums[i-1] > nums[i])
        # left_down[i]: längste alternierende Sequenz, die bei i endet
        #               und deren letzter Vergleich '<' ist (nums[i-1] < nums[i])
        left_up = [1] * n
        left_down = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                left_down[i] = left_up[i-1] + 1
                left_up[i] = 1
            elif nums[i] < nums[i-1]:
                left_up[i] = left_down[i-1] + 1
                left_down[i] = 1
            else:
                left_up[i] = left_down[i] = 1

        # right_up[i] : längste alternierende Sequenz, die bei i beginnt
        #                und deren erster Vergleich '>' ist (nums[i] > nums[i+1])
        # right_down[i]: längste alternierende Sequenz, die bei i beginnt
        #                und deren erster Vergleich '<' ist (nums[i] < nums[i+1])
        right_up = [1] * n
        right_down = [1] * n

        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                right_up[i] = right_down[i+1] + 1
                right_down[i] = 1
            elif nums[i] < nums[i+1]:
                right_down[i] = right_up[i+1] + 1
                right_up[i] = 1
            else:
                right_up[i] = right_down[i] = 1

        # Maximale Länge ohne Entfernung
        max_len = 1
        for i in range(n):
            max_len = max(max_len, left_up[i], left_down[i],
                          right_up[i], right_down[i])

        # Ein Element (nicht am Rand) entfernen und die Lücke schließen
        for i in range(1, n-1):
            a = nums[i-1]
            b = nums[i+1]
            if a == b:
                continue
            if a > b:
                # Der Vergleich zwischen a und b ist '>'.
                # Links wird eine Sequenz benötigt, die mit '<' endet,
                # rechts eine, die mit '<' beginnt.
                cand = left_down[i-1] + right_down[i+1]
                max_len = max(max_len, cand)
            else:  # a < b
                # Vergleich ist '<'.
                # Links Sequenz mit Ende '>', rechts Sequenz mit Beginn '>'.
                cand = left_up[i-1] + right_up[i+1]
                max_len = max(max_len, cand)

        return max_len

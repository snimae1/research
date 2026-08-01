class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        # left_max[i] = Maximum der Elemente links von i
        left_max = [0] * n
        current_max = float('-inf')
        for i in range(n):
            left_max[i] = current_max
            if nums[i] > current_max:
                current_max = nums[i]

        # right_max[i] = Maximum der Elemente rechts von i
        right_max = [0] * n
        current_max = float('-inf')
        for i in range(n - 1, -1, -1):
            right_max[i] = current_max
            if nums[i] > current_max:
                current_max = nums[i]

        result = []
        for i in range(n):
            # Erstes und letztes Element sind immer gültig
            if i == 0 or i == n - 1:
                result.append(nums[i])
            # Ansonsten prüfen, ob eine der Bedingungen erfüllt ist
            elif nums[i] > left_max[i] or nums[i] > right_max[i]:
                result.append(nums[i])

        return result

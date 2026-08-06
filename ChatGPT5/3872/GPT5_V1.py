class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 2:
            return n

        # left[i] = Länge der längsten arithmetischen Teilfolge,
        # die bei i endet.
        left = [1] * n
        left[1] = 2
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 2

        # right[i] = Länge der längsten arithmetischen Teilfolge,
        # die bei i beginnt.
        right = [1] * n
        right[n - 2] = 2
        for i in range(n - 3, -1, -1):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 2

        ans = max(left)

        # Änderung am linken Rand
        ans = max(ans, right[1] + 1)

        # Änderung am rechten Rand
        ans = max(ans, left[n - 2] + 1)

        for i in range(1, n - 1):

            # Fall 1:
            # nums[i] wird so gewählt, dass nums[i-1], nums[i], nums[i+1]
            # arithmetisch werden.
            if (nums[i - 1] + nums[i + 1]) % 2 == 0:
                x = (nums[i - 1] + nums[i + 1]) // 2
                d = x - nums[i - 1]

                l = 1
                if nums[i - 1] - nums[i - 2] == d if i >= 2 else True:
                    l = left[i - 1]

                r = 1
                if nums[i + 2] - nums[i + 1] == d if i + 2 < n else True:
                    r = right[i + 1]

                ans = max(ans, l + 1 + r)

            # Fall 2:
            # Nur nach links erweitern.
            if i >= 2:
                d = nums[i - 1] - nums[i - 2]
                ans = max(ans, left[i - 1] + 1)

            # Fall 3:
            # Nur nach rechts erweitern.
            if i + 2 < n:
                ans = max(ans, right[i + 1] + 1)

        return min(ans, n)

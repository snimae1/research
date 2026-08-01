class Solution(object):
    def maxValue(self, nums1, nums0):
        """
        :type nums1: List[int]
        :type nums0: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums1)

        segments = list(zip(nums1, nums0))

        # Comparator:
        # A before B iff A+B is lexicographically larger than B+A.
        def cmp(a, b):
            a1, a0 = a
            b1, b0 = b

            # Compare the two virtual concatenations without constructing strings.
            i = j = 0
            len1 = a1 + a0 + b1 + b0

            while i < len1:
                # Bit in A+B
                if i < a1:
                    x = 1
                elif i < a1 + a0:
                    x = 0
                elif i < a1 + a0 + b1:
                    x = 1
                else:
                    x = 0

                # Bit in B+A
                if j < b1:
                    y = 1
                elif j < b1 + b0:
                    y = 0
                elif j < b1 + b0 + a1:
                    y = 1
                else:
                    y = 0

                if x != y:
                    return -1 if x > y else 1

                i += 1
                j += 1

            return 0

        from functools import cmp_to_key
        segments.sort(key=cmp_to_key(cmp))

        ans = 0

        for ones, zeros in segments:
            # Append all 1's
            for _ in range(ones):
                ans = (ans * 2 + 1) % MOD

            # Append all 0's
            for _ in range(zeros):
                ans = (ans * 2) % MOD

        return ans

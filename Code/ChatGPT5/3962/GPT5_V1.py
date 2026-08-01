class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = max(nums)

        for l in range(n):
            inside = []
            total = 0

            for r in range(l, n):
                x = nums[r]
                total += x
                inside.append(x)

                m = r - l + 1

                # kleinste Elemente im Intervall
                inside_sorted = sorted(inside)

                # größte positiven Elemente außerhalb
                outside = []
                for i in range(l):
                    if nums[i] > 0:
                        outside.append(nums[i])
                for i in range(r + 1, n):
                    if nums[i] > 0:
                        outside.append(nums[i])

                outside.sort(reverse=True)

                remove = 0
                add = 0
                best = total

                limit = min(k, len(outside), m)

                for t in range(1, limit + 1):
                    remove += inside_sorted[t - 1]
                    add += outside[t - 1]
                    best = max(best, total - remove + add)

                ans = max(ans, best)

        return ans

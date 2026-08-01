class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        # Iterate over all possible divisors k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            m = n // k
            block_max = []
            block_min = []
            valid = True

            # Check each block individually
            for i in range(m):
                start = i * k
                end = start + k

                bmin = nums[start]
                bmax = nums[start]
                drops = 0

                # Check for drops inside the block and find min / max
                for j in range(start, end - 1):
                    if nums[j] > nums[j + 1]:
                        drops += 1
                    if nums[j] < bmin:
                        bmin = nums[j]
                    if nums[j] > bmax:
                        bmax = nums[j]

                # Handle the last element of the block
                if nums[end - 1] < bmin:
                    bmin = nums[end - 1]
                if nums[end - 1] > bmax:
                    bmax = nums[end - 1]

                # Wrap-around drop from last element to first element
                if nums[end - 1] > nums[start]:
                    drops += 1

                # A block can be rotated to sorted order iff it has at most one drop
                if drops > 1:
                    valid = False
                    break

                block_max.append(bmax)
                block_min.append(bmin)

            if not valid:
                continue

            # Check cross-block condition: max of previous block <= min of next block
            for i in range(m - 1):
                if block_max[i] > block_min[i + 1]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans

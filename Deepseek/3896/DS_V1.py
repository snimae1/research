class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Maximum value that we might need to check for primality.
        # Any number in nums can be incremented, but the required target
        # will never be far beyond the original maximum.
        max_val = max(nums) + 200  # generous safety margin for prime gaps
        if max_val < 2:
            max_val = 2

        # Sieve of Eratosthenes
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, max_val + 1, p):
                    is_prime[multiple] = False

        total_ops = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                # even index: must become prime
                if not is_prime[num]:
                    # find the next prime
                    nxt = num
                    while nxt <= max_val and not is_prime[nxt]:
                        nxt += 1
                    total_ops += nxt - num
            else:
                # odd index: must become non-prime
                if is_prime[num]:
                    if num == 2:
                        total_ops += 2  # 2 -> 4
                    else:
                        total_ops += 1  # any other prime -> next integer (even > 2 => composite)
        return total_ops

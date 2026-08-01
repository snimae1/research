from functools import lru_cache

class Solution(object):
    def goodIntegers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        def count_up_to(n):
            if n < 0:
                return 0
            s = str(n)
            
            @lru_cache(maxsize=None)
            def dp(i, prev, tight, started):
                # i: current index in string s
                # prev: previous digit (10 means no previous digit yet / leading zeros)
                # tight: True if the prefix equals n's prefix
                # started: True if we have placed at least one non-zero digit
                if i == len(s):
                    # A number is valid if at least one digit was placed (started).
                    # The number 0 is represented by started=False, but since l >= 10,
                    # including 0 does not affect the final answer.
                    return 1 if started else 0
                
                limit = int(s[i]) if tight else 9
                total = 0
                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    next_started = started or (d != 0)
                    
                    if not next_started:
                        # Still leading zeros, no previous digit constraint
                        total += dp(i + 1, 10, next_tight, False)
                    else:
                        if not started:
                            # Placing the first non-zero digit, no adjacent difference check
                            total += dp(i + 1, d, next_tight, True)
                        else:
                            # Check absolute difference with previous digit
                            if abs(d - prev) <= k:
                                total += dp(i + 1, d, next_tight, True)
                return total
            
            return dp(0, 10, True, False)
        
        return count_up_to(r) - count_up_to(l - 1)

# Optional: quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.goodIntegers(10, 15, 1))   # Expected: 3
    print(sol.goodIntegers(201, 204, 2)) # Expected: 2

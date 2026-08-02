class Solution(object): 

    def longestAlternating(self, nums): 

        """ 

        :type nums: List[int] 

        :rtype: int 

        """ 

        n = len(nums) 

  

        def sign(a, b): 

            if a < b: 

                return 1 

            elif a > b: 

                return -1 

            else: 

                return 0 

  

        left = [1] * n 

        for i in range(1, n): 

            if sign(nums[i - 1], nums[i]) != 0: 

                if i == 1 or sign(nums[i - 2], nums[i - 1]) == 0 or sign(nums[i - 2], nums[i - 1]) == sign(nums[i - 1], nums[i]): 

                    left[i] = 2 

                else: 

                    left[i] = left[i - 1] + 1 

  

        right = [1] * n 

        for i in range(n - 2, -1, -1): 

            if sign(nums[i], nums[i + 1]) != 0: 

                if i == n - 2 or sign(nums[i + 1], nums[i + 2]) == 0 or sign(nums[i], nums[i + 1]) == sign(nums[i + 1], nums[i + 2]): 

                    right[i] = 2 

                else: 

                    right[i] = right[i + 1] + 1 

  

        res = max(left) 

  

        for i in range(n): 

            if i == 0: 

                res = max(res, right[1]) 

            elif i == n - 1: 

                res = max(res, left[n - 2]) 

            else: 

                s1 = sign(nums[i - 1], nums[i + 1]) 

                if s1 == 0: 

                    continue 

  

                if i >= 2: 

                    s0 = sign(nums[i - 2], nums[i - 1]) 

                    if s0 != 0 and s0 != s1: 

                        left_len = left[i - 1] 

                    else: 

                        left_len = 2 

                else: 

                    left_len = 2 

  

                if i <= n - 3: 

                    s2 = sign(nums[i + 1], nums[i + 2]) 

                    if s2 != 0 and s1 != s2: 

                        right_len = right[i + 1] 

                    else: 

                        right_len = 2 

                else: 

                    right_len = 2 

  

                res = max(res, left_len + right_len - 1) 

  

        return res

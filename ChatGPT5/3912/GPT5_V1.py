class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Maximales Element links von jeder Position
        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i])
        
        # Maximales Element rechts von jeder Position
        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        
        result = []
        
        for i in range(n):
            # Erstes und letztes Element sind immer gültig
            if i == 0 or i == n-1:
                result.append(nums[i])
            else:
                # Strikt größer als alles links oder alles rechts
                if nums[i] > left_max[i-1] or nums[i] > right_max[i+1]:
                    result.append(nums[i])
        
        return result

class Solution(object):

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Die minimale Summe der Erhöhungen x ist die Summe aller 
        # Differenzen an den Stellen, an denen das Array abfällt.
        # Wenn nums[i] > nums[i+1], muss mindestens dieser Unterschied 
        # durch eine Operation (und ein entsprechendes Subarray) ausgeglichen werden.
        
        total_x_sum = 0
        n = len(nums)
        
        for i in range(n - 1):
            # Wir suchen nach "Drops" im Array
            if nums[i] > nums[i + 1]:
                # Die Differenz muss zwingend durch x-Werte kompensiert werden.
                # Da wir Subarrays nutzen können, ist es am effizientesten, 
                # den Rest des Arrays mitzuerhöhen, sodass keine neuen 
                # Differenzen entstehen.
                total_x_sum += nums[i] - nums[i + 1]
        
        return total_x_sum

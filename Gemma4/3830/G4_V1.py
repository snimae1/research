class Solution(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        
        # dp_left[i][0]: Länge der alternierenden Folge, die bei i endet mit einem Anstieg (nums[i-1] < nums[i])
        # dp_left[i][1]: Länge der alternierenden Folge, die bei i endet mit einem Abfall (nums[i-1] > nums[i])
        dp_left = [[1, 1] for _ in range(n)]
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp_left[i][0] = dp_left[i-1][1] + 1
            elif nums[i] < nums[i-1]:
                dp_left[i][1] = dp_left[i-1][0] + 1
        
        # dp_right[i][0]: Länge der alternierenden Folge, die bei i beginnt mit einem Anstieg (nums[i] < nums[i+1])
        # dp_right[i][1]: Länge der alternierenden Folge, die bei i beginnt mit einem Abfall (nums[i] > nums[i+1])
        dp_right = [[1, 1] for _ in range(n)]
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                dp_right[i][0] = dp_right[i+1][1] + 1
            elif nums[i] > nums[i+1]:
                dp_right[i][1] = dp_right[i+1][0] + 1
        
        # Basiswert: Die längste alternierende Folge ohne Entfernung eines Elements
        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp_left[i][0], dp_left[i][1])
            
        # Wir versuchen nun, jedes Element i zu entfernen und die Lücke zu schließen
        for i in range(1, n - 1):
            # Wenn wir nums[i] entfernen, prüfen wir die Verbindung zwischen nums[i-1] und nums[i+1]
            if nums[i-1] < nums[i+1]:
                # Brücke ist ein Anstieg (<). 
                # Links muss also mit einem Abfall enden (dp_left[i-1][1])
                # Rechts muss mit einem Abfall beginnen (dp_right[i+1][1])
                max_len = max(max_len, dp_left[i-1][1] + dp_right[i+1][1])
            elif nums[i-1] > nums[i+1]:
                # Brücke ist ein Abfall (>).
                # Links muss mit einem Anstieg enden (dp_left[i-1][0])
                # Rechts muss mit einem Anstieg beginnen (dp_right[i+1][0])
                max_len = max(max_len, dp_left[i-1][0] + dp_right[i+1][0])
        
        return max_len

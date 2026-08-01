class Solution(object):

    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """ 
        # Wir verwandeln die gesuchte Ziffer in einen String, 
        # damit wir sie im Text der Zahlen suchen können.
        digit_str = str(digit)
        total_count = 0
        
        for num in nums:
            # Jede Zahl wird in einen String umgewandelt und die Vorkommen gezählt
            total_count += str(num).count(digit_str)
            
        return total_count

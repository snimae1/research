class Solution(object):
    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # active = 0 for first player, 1 for second player
        active = 0
        score1 = 0
        score2 = 0
        
        for i, points in enumerate(nums):
            # Rule 1: if points are odd, swap active/inactive
            if points % 2 == 1:
                active = 1 - active
            
            # Rule 2: every 6th game (indices 5, 11, 17, ...) swap again
            if i % 6 == 5:
                active = 1 - active
            
            # The active player gains points
            if active == 0:
                score1 += points
            else:
                score2 += points
        
        return score1 - score2

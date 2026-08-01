class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Zähle die Gesamtzahl aller '0'en und '1'en im String
        zeros = s.count('0')
        ones = s.count('1')
        
        # Ein balancierter String benötigt immer gleich viele 0en und 1en.
        # Die maximale Anzahl an Paaren (0,1), die wir bilden können, 
        # ist durch das Zeichen begrenzt, von dem wir am wenigsten haben.
        # Da wir einen Swap durchführen können, um die Zeichen optimal 
        # zu platzieren, ist die maximale Länge einfach 2 * min(zeros, ones).
        return 2 * min(zeros, ones)

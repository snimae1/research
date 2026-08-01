class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        # Zahl in String umwandeln, damit einzelne Ziffern geprüft werden können
        s = str(n)
        
        # Prüfen, ob die Zahl mit x beginnt
        if s[0] == str(x):
            return False
        
        # Prüfen, ob x irgendwo in der Zahl vorkommt
        if str(x) in s:
            return True
        
        return False

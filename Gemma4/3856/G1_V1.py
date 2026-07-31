class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # .rstrip() entfernt alle angegebenen Zeichen vom rechten Ende des Strings,
        # bis ein Zeichen auftaucht, das nicht in der Liste enthalten ist.
        return s.rstrip('aeiou')

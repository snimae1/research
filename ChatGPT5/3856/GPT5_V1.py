class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiou")

        i = len(s) - 1
        while i >= 0 and s[i] in vowels:
            i -= 1

        return s[:i + 1]

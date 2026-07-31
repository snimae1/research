class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1:
            return 0
        if n == 2:
            return 0 if s[0] <= s[1] else -1

        # Check if s is already sorted
        sorted_flag = True
        min_c = s[0]
        max_c = s[0]

        for i, ch in enumerate(s):
            if ch < min_c:
                min_c = ch
            if ch > max_c:
                max_c = ch
            if i > 0 and s[i] < s[i-1]:
                sorted_flag = False

        if sorted_flag:
            return 0

        # 1 operation is enough if the first character is already the global minimum
        # or the last character is already the global maximum.
        if s[0] == min_c or s[-1] == max_c:
            return 1

        # Otherwise we need to see if we can fix an endpoint in one move.
        min_not_only_last = False
        max_not_only_first = False

        for i, ch in enumerate(s):
            if ch == min_c and i < n - 1:
                min_not_only_last = True
            if ch == max_c and i > 0:
                max_not_only_first = True
            if min_not_only_last and max_not_only_first:
                break

        if min_not_only_last or max_not_only_first:
            return 2
        return 3

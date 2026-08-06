class Solution(object):
    def countGoodSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        # prev[or_value] = größte Startposition eines Subarrays,
        # das am vorherigen Index endet und diesen OR-Wert besitzt.
        prev = {}

        for i in range(n):
            cur = {}

            # Neues Subarray [i]
            cur[nums[i]] = i

            # Alle Subarrays erweitern
            for or_val, start in prev.items():
                new_or = or_val | nums[i]
                if new_or in cur:
                    if start > cur[new_or]:
                        cur[new_or] = start
                else:
                    cur[new_or] = start

            # Für jeden möglichen OR-Wert prüfen,
            # ob er als Element im Subarray vorkommt.
            best = -1
            for or_val, start in cur.items():
                if or_val == nums[i]:
                    if start > best:
                        best = start

            # Jetzt müssen wir noch frühere Vorkommen des OR-Werts kennen.
            # last_pos speichert die letzte Position jedes Wertes.
            if i == 0:
                last_pos = {}
            last_pos[nums[i]] = i

            # Alle Kandidaten erneut prüfen
            for or_val, start in cur.items():
                if or_val in last_pos:
                    pos = last_pos[or_val]
                    if pos >= start:
                        if pos > best:
                            best = pos

            if best != -1:
                ans += best + 1

            prev = cur

        return ans

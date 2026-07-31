from collections import Counter

class Solution(object):
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)

        # Jeder Wert muss insgesamt gerade oft vorkommen.
        total = Counter(nums1)
        total.update(nums2)

        for cnt in total.values():
            if cnt & 1:
                return -1

        # diff[v]:
        # >0 => zu viele v in nums1
        # <0 => zu viele v in nums2
        diff = Counter()
        for x in nums1:
            diff[x] += 1
        for x in nums2:
            diff[x] -= 1

        # Anzahl der Werte, die von nums1 nach nums2 verschoben werden müssen.
        need = 0
        for d in diff.values():
            if d > 0:
                need += d // 2

        # Jeder Index mit unterschiedlichen Werten kann höchstens einen
        # Überschusswert transportieren.
        mismatch_capacity = 0
        for a, b in zip(nums1, nums2):
            if a != b:
                mismatch_capacity += 1

        if need > mismatch_capacity:
            return -1

        return need

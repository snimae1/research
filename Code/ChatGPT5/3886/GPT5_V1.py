class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)

        # Alle Teiler von n
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1

        ans = 0

        for k in divisors:
            ok = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if k == 1:
                    if a[0] != b[0]:
                        ok = False
                        break
                    continue

                # Multimenge muss identisch sein
                if sorted(a) != b:
                    ok = False
                    break

                # Prüfen, ob b eine Rotation von a ist
                aa = a + a
                found = False

                for shift in range(k):
                    good = True
                    for j in range(k):
                        if aa[shift + j] != b[j]:
                            good = False
                            break
                    if good:
                        found = True
                        break

                if not found:
                    ok = False
                    break

            if ok:
                ans += k

        return ans

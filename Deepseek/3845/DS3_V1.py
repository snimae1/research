from typing import List
from collections import deque

class Trie:
    def __init__(self, max_bits=15):
        self.max_bits = max_bits
        # each node: [left_child, right_child, count]
        self.children = [[-1, -1]]
        self.cnt = [0]

    def insert(self, num: int) -> None:
        node = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if self.children[node][0] == -1:
                    self.children.append([-1, -1])
                    self.cnt.append(0)
                    self.children[node][0] = len(self.children) - 1
                node = self.children[node][0]
            else:
                if self.children[node][1] == -1:
                    self.children.append([-1, -1])
                    self.cnt.append(0)
                    self.children[node][1] = len(self.children) - 1
                node = self.children[node][1]
            self.cnt[node] += 1

    def remove(self, num: int) -> None:
        node = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                node = self.children[node][0]
            else:
                node = self.children[node][1]
            self.cnt[node] -= 1

    def query(self, num: int) -> int:
        node = 0
        xor_val = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                # try to go to 1 (opposite) to get a 1 in xor
                if self.children[node][1] != -1 and self.cnt[self.children[node][1]] > 0:
                    xor_val |= (1 << i)
                    node = self.children[node][1]
                else:
                    node = self.children[node][0]
            else:
                # try to go to 0 (opposite) to get a 1 in xor
                if self.children[node][0] != -1 and self.cnt[self.children[node][0]] > 0:
                    xor_val |= (1 << i)
                    node = self.children[node][0]
                else:
                    node = self.children[node][1]
        return xor_val


class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # prefix xor: pref[i] = xor of nums[0..i-1]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]

        # deques for sliding window min/max
        max_dq = deque()
        min_dq = deque()

        trie = Trie(max_bits=15)
        left = 0
        ans = 0

        for right in range(n):
            val = nums[right]

            # maintain max deque
            while max_dq and nums[max_dq[-1]] <= val:
                max_dq.pop()
            max_dq.append(right)

            # maintain min deque
            while min_dq and nums[min_dq[-1]] >= val:
                min_dq.pop()
            min_dq.append(right)

            # shrink window until max - min <= k
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                # remove nums[left] from deques if it is at the front
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()

                # pref[left] is no longer a valid starting prefix for subarrays
                # ending at or after right, so remove it from the trie
                trie.remove(pref[left])
                left += 1

            # pref[right] becomes a valid start for subarrays ending at right
            trie.insert(pref[right])

            # query the best xor with pref[right+1]
            best = trie.query(pref[right + 1])
            if best > ans:
                ans = best

        return ans

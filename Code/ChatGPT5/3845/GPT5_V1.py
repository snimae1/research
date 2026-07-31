from collections import deque

class TrieNode(object):
    __slots__ = ("child", "cnt")

    def __init__(self):
        self.child = [None, None]
        self.cnt = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, x):
        node = self.root
        node.cnt += 1
        for b in range(14, -1, -1):
            bit = (x >> b) & 1
            if node.child[bit] is None:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.cnt += 1

    def erase(self, x):
        node = self.root
        node.cnt -= 1
        for b in range(14, -1, -1):
            bit = (x >> b) & 1
            node = node.child[bit]
            node.cnt -= 1

    def query(self, x):
        node = self.root
        ans = 0
        for b in range(14, -1, -1):
            bit = (x >> b) & 1
            want = bit ^ 1
            if node.child[want] is not None and node.child[want].cnt > 0:
                ans |= (1 << b)
                node = node.child[want]
            else:
                node = node.child[bit]
        return ans


class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Prefix XOR
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ nums[i]

        minq = deque()
        maxq = deque()

        trie = Trie()
        trie.insert(pre[0])

        left = 0
        remove_ptr = 0
        ans = 0

        for r in range(n):
            while minq and nums[minq[-1]] >= nums[r]:
                minq.pop()
            minq.append(r)

            while maxq and nums[maxq[-1]] <= nums[r]:
                maxq.pop()
            maxq.append(r)

            while nums[maxq[0]] - nums[minq[0]] > k:
                if minq[0] == left:
                    minq.popleft()
                if maxq[0] == left:
                    maxq.popleft()
                left += 1

            while remove_ptr < left:
                trie.erase(pre[remove_ptr])
                remove_ptr += 1

            ans = max(ans, trie.query(pre[r + 1]))
            trie.insert(pre[r + 1])

        return ans

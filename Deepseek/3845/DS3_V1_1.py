import collections

class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # prefix xor
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] ^ nums[i]
        
        BITS = 15  # numbers are < 2^15
        # Trie implemented with a list: [child0, child1, count]
        trie = [[-1, -1, 0]]
        
        def insert(num):
            node = 0
            for i in range(BITS-1, -1, -1):
                b = (num >> i) & 1
                if trie[node][b] == -1:
                    trie[node][b] = len(trie)
                    trie.append([-1, -1, 0])
                node = trie[node][b]
                trie[node][2] += 1
        
        def delete(num):
            node = 0
            for i in range(BITS-1, -1, -1):
                b = (num >> i) & 1
                node = trie[node][b]
                trie[node][2] -= 1
        
        def maxXor(num):
            node = 0
            ans = 0
            for i in range(BITS-1, -1, -1):
                b = (num >> i) & 1
                desired = 1 - b
                child = trie[node][desired]
                if child != -1 and trie[child][2] > 0:
                    ans |= (1 << i)
                    node = child
                else:
                    node = trie[node][b]
            return ans
        
        insert(pref[0])
        L = 0
        maxd = collections.deque()
        mind = collections.deque()
        ans = 0
        
        for R in range(n):
            val = nums[R]
            # maintain max deque
            while maxd and nums[maxd[-1]] <= val:
                maxd.pop()
            maxd.append(R)
            # maintain min deque
            while mind and nums[mind[-1]] >= val:
                mind.pop()
            mind.append(R)
            
            # shrink window while max - min > k
            while maxd and mind and nums[maxd[0]] - nums[mind[0]] > k:
                if maxd[0] == L:
                    maxd.popleft()
                if mind[0] == L:
                    mind.popleft()
                delete(pref[L])
                L += 1
            
            # query max xor for subarrays ending at R
            cur = maxXor(pref[R+1])
            if cur > ans:
                ans = cur
                
            # insert current prefix for future queries
            insert(pref[R+1])
            
        return ans

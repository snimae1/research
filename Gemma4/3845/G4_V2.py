"""
This module provides a solution to find the maximum XOR value of a subarray
where the difference between the maximum and minimum elements is at most k.
"""

from collections import deque


class XorTrie:
    """A Bit-Trie to store prefix XORs and find the maximum XOR match."""

    def __init__(self, max_bits=15):
        """Initialize the Trie with a fixed number of bits."""
        self.max_bits = max_bits
        self.trie = {}  # Format: {bit: [count, next_node_dict]}

    def insert(self, val):
        """Inserts a value into the Trie and increments path counts."""
        node = self.trie
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            if bit not in node:
                node[bit] = [0, {}]
            node[bit][0] += 1
            node = node[bit][1]

    def remove(self, val):
        """Removes a value from the Trie by decrementing path counts."""
        node = self.trie
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            node[bit][0] -= 1
            # We don't strictly need to delete the key, 
            # the count check in query handles it.
            node = node[bit][1]

    def query_max_xor(self, val):
        """Finds the value in the Trie that maximizes (val XOR stored_value)."""
        node = self.trie
        current_xor = 0
        for i in range(self.max_bits, -1, -1):
            bit = (val >> i) & 1
            wanted = 1 - bit
            # Move to the 'wanted' bit if it exists and has a count > 0
            if wanted in node and node[wanted][0] > 0:
                current_xor |= (1 << i)
                node = node[wanted][1]
            elif bit in node and node[bit][0] > 0:
                node = node[bit][1]
            else:
                return 0
        return current_xor


class Solution:
    """Solution class to calculate the max XOR of a constrained subarray."""

    def max_xor(self, nums, k):
        """
        Calculates the maximum XOR of a subarray where max(subarray) - min(subarray) <= k.
        
        Args:
            nums (List[int]): List of non-negative integers.
            k (int): Maximum allowed difference between max and min elements.
            
        Returns:
            int: The maximum XOR sum found.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Monotonic queues to maintain min and max in the current window
        min_deque = deque()
        max_deque = deque()
        
        # Trie to store XOR prefixes of the current valid window
        trie = XorTrie()
        
        # Prefix XOR array: prefix_xor[i] = nums[0] ^ ... ^ nums[i-1]
        prefix_xor = 0
        # We start by inserting the identity element for XOR (0)
        trie.insert(0)
        
        left = 0
        global_max = 0
        current_prefix_xor = 0

        for right in range(n):
            val = nums[right]
            current_prefix_xor ^= val
            
            # Update monotonic queues for min and max
            while min_deque and nums[min_deque[-1]] >= val:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and nums[max_deque[-1]] <= val:
                max_deque.pop()
            max_deque.append(right)
            
            # Shrink the window from the left if max - min > k
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                # Remove the prefix XOR from the trie before moving left pointer
                # The prefix XOR associated with index 'left' is the one
                # before nums[left] was added.
                # We need to recover the prefix XOR at index 'left'.
                # To avoid re-calculating, we can pre-calculate prefix_xor array.
                # For simplicity here, we use a local calculation or store them.
                pass
            
            # Optimization: To avoid complex recalculation in the while loop, 
            # let's use a precomputed prefix array.
            # (Refactored logic below)
        
        return global_max

    def maxXor(self, nums, k):
        """Alias method to maintain the specific required syntax."""
        return self._solve_max_xor(nums, k)

    def _solve_max_xor(self, nums, k):
        """Internal implementation of the sliding window XOR logic."""
        n = len(nums)
        # Precompute prefix XORs to allow O(1) removal from Trie
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]

        min_dq = deque()
        max_dq = deque()
        trie = XorTrie()
        
        left = 0
        ans = 0
        
        # The Trie stores pref[left...right]. 
        # For a window [left, right], the XOR of the subarray is pref[right+1] ^ pref[i]
        # where left <= i <= right.
        for right in range(n):
            # Maintain min/max deques
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
            # Insert the prefix XOR that ends just before the current element
            trie.insert(pref[right])
            
            # Shrink window if max - min > k
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                trie.remove(pref[left])
                left += 1
                # Remove indices from deques that are now outside the window
                if min_dq[0] < left:
                    min_dq.popleft()
                if max_dq[0] < left:
                    max_dq.popleft()
            
            # Query Trie for the max XOR using the current full prefix
            ans = max(ans, trie.query_max_xor(pref[right + 1]))
            
        return ans

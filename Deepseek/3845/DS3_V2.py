"""
Module for solving the maximum XOR subarray problem with a constraint on max-min difference.
"""

from typing import List
from collections import deque


class Trie:
    """
    A binary trie that supports insert, remove, and query maximum XOR with a given number.
    The numbers are assumed to have at most 15 bits (since nums[i] < 2^15).
    """

    def __init__(self, max_bits: int = 15):
        self.max_bits = max_bits
        # Each node is represented as [left_child_index, right_child_index]
        self.children = [[-1, -1]]
        # Count of numbers passing through each node
        self.counts = [0]

    def insert(self, num: int) -> None:
        """Insert a number into the trie."""
        node = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if self.children[node][0] == -1:
                    self.children.append([-1, -1])
                    self.counts.append(0)
                    self.children[node][0] = len(self.children) - 1
                node = self.children[node][0]
            else:
                if self.children[node][1] == -1:
                    self.children.append([-1, -1])
                    self.counts.append(0)
                    self.children[node][1] = len(self.children) - 1
                node = self.children[node][1]
            self.counts[node] += 1

    def remove(self, num: int) -> None:
        """Remove a number from the trie (decrement counts)."""
        node = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                node = self.children[node][0]
            else:
                node = self.children[node][1]
            self.counts[node] -= 1

    def query(self, num: int) -> int:
        """
        Return the maximum XOR value possible by XORing num with any number currently in the trie.
        """
        node = 0
        xor_val = 0
        for i in range(self.max_bits - 1, -1, -1):
            bit = (num >> i) & 1
            # We prefer to take the opposite bit to get a 1 in the XOR result.
            if bit == 0:
                if self.children[node][1] != -1 and self.counts[self.children[node][1]] > 0:
                    xor_val |= (1 << i)
                    node = self.children[node][1]
                else:
                    node = self.children[node][0]
            else:
                if self.children[node][0] != -1 and self.counts[self.children[node][0]] > 0:
                    xor_val |= (1 << i)
                    node = self.children[node][0]
                else:
                    node = self.children[node][1]
        return xor_val


class Solution:
    """
    Solution class for the maximum XOR subarray problem.
    """

    def maxXor(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum XOR value of any subarray whose max-min difference <= k.

        Args:
            nums (List[int]): Non-negative integers less than 2^15.
            k (int): Allowed difference between max and min.

        Returns:
            int: Maximum XOR value.
        """
        n = len(nums)
        # prefix XORs: pref[i] = XOR of nums[0..i-1]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]

        # Deques for sliding window min/max
        max_dq = deque()
        min_dq = deque()

        trie = Trie(max_bits=15)  # Since nums[i] < 2^15, prefix XORs also < 2^15.
        left = 0
        ans = 0

        for right in range(n):
            val = nums[right]

            # Maintain decreasing deque for max
            while max_dq and nums[max_dq[-1]] <= val:
                max_dq.pop()
            max_dq.append(right)

            # Maintain increasing deque for min
            while min_dq and nums[min_dq[-1]] >= val:
                min_dq.pop()
            min_dq.append(right)

            # Shrink window until condition is satisfied
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                # Remove the leftmost element from deques if it is at the front
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()

                # The prefix XOR at 'left' is no longer a valid starting point
                # for subarrays ending at or after 'right', so remove it from trie.
                trie.remove(pref[left])
                left += 1

            # Add pref[right] as a valid starting prefix for subarrays ending at 'right'
            trie.insert(pref[right])

            # Query the best XOR with pref[right+1]
            best = trie.query(pref[right + 1])
            ans = max(ans, best)

        return ans

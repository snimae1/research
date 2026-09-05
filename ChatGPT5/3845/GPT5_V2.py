"""Find the maximum XOR of a subarray with a bounded value range."""

from collections import deque


class TrieNode:
    """Node of a binary trie used for maximum-XOR queries."""

    def __init__(self):
        """Create an empty trie node."""
        self.children = [None, None]
        self.count = 0


class BinaryTrie:
    """Binary trie supporting insertion, deletion and maximum-XOR queries."""

    def __init__(self):
        """Create an empty binary trie."""
        self.root = TrieNode()

    def insert(self, value):
        """Add one value to the trie."""
        node = self.root
        node.count += 1

        for bit_position in range(14, -1, -1):
            bit = (value >> bit_position) & 1

            if node.children[bit] is None:
                node.children[bit] = TrieNode()

            node = node.children[bit]
            node.count += 1

    def remove(self, value):
        """Remove one occurrence of a value from the trie."""
        node = self.root
        node.count -= 1

        for bit_position in range(14, -1, -1):
            bit = (value >> bit_position) & 1
            node = node.children[bit]
            node.count -= 1

    def maximum_xor(self, value):
        """Return the largest XOR obtainable with a stored value."""
        node = self.root
        result = 0

        # Prefer the opposite bit at every position because it
        # contributes a 1 to the resulting XOR.
        for bit_position in range(14, -1, -1):
            bit = (value >> bit_position) & 1
            preferred_bit = bit ^ 1

            preferred_child = node.children[preferred_bit]

            if preferred_child is not None and preferred_child.count > 0:
                result |= 1 << bit_position
                node = preferred_child
            else:
                node = node.children[bit]

        return result


class Solution:
    """Solve the maximum-XOR subarray problem."""

    # The judge requires the method name maxXor.
    def maxXor(self, nums, k):  # pylint: disable=invalid-name
        """
        Return the maximum XOR of a valid contiguous subarray.

        A subarray is valid when max(subarray) - min(subarray) <= k.

        :param nums: Non-negative integers.
        :param k: Maximum allowed difference between maximum and minimum.
        :return: Maximum XOR of any valid subarray.
        """
        n = len(nums)

        # prefix_xor[i] is the XOR of nums[0:i].
        # Therefore:
        #
        # XOR(nums[left:right + 1]) =
        # prefix_xor[right + 1] XOR prefix_xor[left]
        prefix_xor = [0] * (n + 1)

        for index, value in enumerate(nums):
            prefix_xor[index + 1] = prefix_xor[index] ^ value

        # The deques contain indices rather than values.
        #
        # min_queue: values increase from front to back.
        # max_queue: values decrease from front to back.
        #
        # This lets us find the minimum and maximum of the current
        # sliding window in O(1).
        min_queue = deque()
        max_queue = deque()

        trie = BinaryTrie()

        # Before processing the first element, prefix_xor[0] represents
        # the empty prefix and can be used as the left boundary.
        trie.insert(prefix_xor[0])

        left = 0
        removed_prefix = 0
        maximum_xor = 0

        for right, value in enumerate(nums):
            # Maintain the monotonic queue for the minimum.
            while min_queue and nums[min_queue[-1]] >= value:
                min_queue.pop()

            min_queue.append(right)

            # Maintain the monotonic queue for the maximum.
            while max_queue and nums[max_queue[-1]] <= value:
                max_queue.pop()

            max_queue.append(right)

            # If the window is invalid, move its left boundary to the
            # right until max - min <= k again.
            while nums[max_queue[0]] - nums[min_queue[0]] > k:
                if min_queue[0] == left:
                    min_queue.popleft()

                if max_queue[0] == left:
                    max_queue.popleft()

                left += 1

            # Only prefix XORs whose corresponding left boundary is
            # inside the current valid window may be used.
            while removed_prefix < left:
                trie.remove(prefix_xor[removed_prefix])
                removed_prefix += 1

            # For subarray [left ... right], we need
            #
            # prefix_xor[right + 1] XOR prefix_xor[left].
            #
            # The trie finds the best possible prefix_xor[left].
            current_xor = trie.maximum_xor(prefix_xor[right + 1])
            maximum_xor = max(maximum_xor, current_xor)

            # This prefix can become a left boundary for future windows.
            trie.insert(prefix_xor[right + 1])

        return maximum_xor

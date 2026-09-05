"""Find the smallest suitable box for an item."""

class Solution:
"""Provide a solution for finding the best box."""

```
def minimumIndex(self, capacity, itemSize):
    """
    Find the index of the smallest box that can hold the item.

    :param capacity: Capacities of all available boxes.
    :param itemSize: Size of the item to store.
    :return: Index of the suitable box with the smallest capacity,
             or -1 if no box is large enough.
    """
    best_index = -1
    best_capacity = float("inf")

    for index, box_capacity in enumerate(capacity):
        # Update only for a smaller capacity, keeping the first index
        # when multiple boxes have the same capacity.
        if itemSize <= box_capacity < best_capacity:
            best_capacity = box_capacity
            best_index = index

    return best_index
```

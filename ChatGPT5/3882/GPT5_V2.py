"""Find the minimum XOR value among all valid paths in a grid."""

# pylint: disable=invalid-name,too-few-public-methods,useless-object-inheritance


class Solution(object):
    """Solve the minimum XOR path problem."""

    XOR_VALUES = 1024

    @staticmethod
    def _next_xors(previous_xors, cell_value):
        """Calculate XOR values after entering the current cell."""
        result = [False] * Solution.XOR_VALUES

        for xor_value, reachable in enumerate(previous_xors):
            if reachable:
                result[xor_value ^ cell_value] = True

        return result

    def minCost(self, grid):
        """
        Find the minimum XOR value of a path from top-left to bottom-right.

        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])

        # dp[column] contains all XOR values reachable at the
        # current row and this column.
        dp = [None] * columns

        for row in range(rows):
            current_row = [None] * columns

            for column in range(columns):
                cell_value = grid[row][column]

                if row == 0 and column == 0:
                    reachable = [False] * Solution.XOR_VALUES
                    reachable[cell_value] = True
                else:
                    reachable = [False] * Solution.XOR_VALUES

                    # We can arrive from the cell above.
                    if row > 0:
                        reachable = Solution._merge_xors(
                            reachable,
                            Solution._next_xors(dp[column], cell_value)
                        )

                    # We can arrive from the cell on the left.
                    if column > 0:
                        reachable = Solution._merge_xors(
                            reachable,
                            Solution._next_xors(
                                current_row[column - 1],
                                cell_value
                            )
                        )

                current_row[column] = reachable

            dp = current_row

        # The first reachable XOR value is the smallest one.
        result = 0
        while not dp[columns - 1][result]:
            result += 1

        return result

    @staticmethod
    def _merge_xors(first, second):
        """Merge two sets of reachable XOR values."""
        for index, reachable in enumerate(second):
            if reachable:
                first[index] = True

        return first
